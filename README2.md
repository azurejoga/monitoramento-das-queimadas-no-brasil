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
| 6b54b475-2c87-36a3-a586-047072c2c1f5 | -18.3731 | -43.104 | 2024-10-08 00:04:12 | METOP-B | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd813be4-b8b0-3b1c-978b-2315596833a0 | -17.6656 | -41.1189 | 2024-10-08 00:04:17 | METOP-B | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83a96afc-a532-3aff-95c5-92d1937854e0 | -17.6672 | -41.126801 | 2024-10-08 00:04:17 | METOP-B | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37195e37-f37f-30f0-8b97-37ab3aff82b3 | -11.32 | -51.02 | 2024-10-08 00:04:21 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20c0ed09-19b0-3536-ae02-81bb3b6d5e60 | -11.29 | -51.07 | 2024-10-08 00:04:21 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34e09b45-141d-3335-933a-711b9b668a8d | -11.32 | -51.08 | 2024-10-08 00:04:21 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e627a544-de77-39bb-a5b5-ddcf1c859408 | -11.35 | -51.09 | 2024-10-08 00:04:21 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2bbd3a0b-28fd-3a85-9cb6-594144212a9d | -11.35 | -51.03 | 2024-10-08 00:04:21 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9c9b500-d5ca-3f29-86b7-1cf9d44b09d1 | -18.1043 | -45.0439 | 2024-10-08 00:04:23 | METOP-B | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9b95128a-fda4-3040-a9d8-117cde4d2213 | -18.994801 | -50.148399 | 2024-10-08 00:04:23 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6abd0e13-b021-3405-b102-11ad5ae8f5ed | -18.999399 | -50.177101 | 2024-10-08 00:04:23 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82bed822-3d8d-3ac2-b186-a1de451dae85 | -18.989799 | -50.178699 | 2024-10-08 00:04:23 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| db9eb40c-cf68-381b-9f1e-8ebd0ea100ed | -18.917601 | -50.1614 | 2024-10-08 00:04:24 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7543567a-3622-3f82-b919-baaf7259c28b | -18.922199 | -50.190201 | 2024-10-08 00:04:24 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c38c5d77-3b5c-3697-b608-f22343314343 | -18.9079 | -50.162998 | 2024-10-08 00:04:24 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 99d46c20-03a3-37fe-a31a-511142fbb364 | -18.9125 | -50.191799 | 2024-10-08 00:04:24 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 33803dd7-adf3-3611-8fa8-5fb53a845395 | -18.917101 | -50.220699 | 2024-10-08 00:04:24 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a3cf311d-e6b0-3588-827f-cacf4cbb57e1 | -18.8983 | -50.1646 | 2024-10-08 00:04:24 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d5339056-1dc4-3f6c-9c0a-e41d2b702146 | -17.6588 | -43.357899 | 2024-10-08 00:04:25 | METOP-B | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c3e522d-f183-37a5-b34f-682c8cc16575 | -17.657301 | -43.870602 | 2024-10-08 00:04:26 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9ed0707-cbd6-3188-9e86-234855cc3edb | -17.6593 | -43.881199 | 2024-10-08 00:04:26 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 034009b5-4cc2-3db9-8b6a-1b07a5b8f160 | -18.1637 | -48.481499 | 2024-10-08 00:04:32 | METOP-B | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c3bcc5e3-f3c7-34fd-8f86-28ce11f7c937 | -16.2985 | -42.033199 | 2024-10-08 00:04:43 | METOP-B | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5ebc0c71-d679-32d1-aa6e-7a953da06fb3 | -14.9644 | -41.875401 | 2024-10-08 00:05:04 | METOP-B | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f22eb11a-a2cc-3b53-b92e-0c148f1ca9ec | -14.9522 | -42.353901 | 2024-10-08 00:05:06 | METOP-B | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d541fb95-161d-324b-a0d2-ee5ab3319490 | -16.0861 | -50.119999 | 2024-10-08 00:05:11 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd493165-da31-3caa-b7bb-f7b7b5d4b3f8 | -16.090599 | -50.146 | 2024-10-08 00:05:11 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c35a5c47-cd91-37d0-8fbd-38d78dcc5f30 | -16.0951 | -50.1721 | 2024-10-08 00:05:11 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 35ab978a-9076-3ed6-a2cb-f7bce8d4ef32 | -16.0809 | -50.147701 | 2024-10-08 00:05:11 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 61adcb1e-fd5d-3142-87db-2445f50d7e64 | -14.5114 | -42.450199 | 2024-10-08 00:05:13 | METOP-B | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c516be2e-66fc-3d51-866f-a53fa0e26fa1 | -14.5131 | -42.458302 | 2024-10-08 00:05:13 | METOP-B | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 818a77b7-4d00-36f0-8fa6-11b48a5ca0f4 | -14.5334 | -43.196499 | 2024-10-08 00:05:15 | METOP-B | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0271bea9-03da-38f2-9b3e-2b4efdae496b | -14.5352 | -43.205299 | 2024-10-08 00:05:15 | METOP-B | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0a7e425d-131f-3878-8e8c-0fc321334178 | -14.5371 | -43.2141 | 2024-10-08 00:05:15 | METOP-B | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c4daa79-4dca-3764-b10b-a2978b358c12 | -14.8885 | -45.107899 | 2024-10-08 00:05:16 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| be5e2512-32e6-3740-a6ad-1aa469a9192c | -14.4263 | -43.770401 | 2024-10-08 00:05:19 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2745a094-7916-3099-9c72-d1eb50078bc8 | -14.011 | -42.458 | 2024-10-08 00:05:21 | METOP-B | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2d74a4ea-c273-34ea-a89e-35b927f32e84 | -14.0127 | -42.466099 | 2024-10-08 00:05:21 | METOP-B | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7eb2cd9c-19c3-3042-811e-930fadd0c080 | -2.7985 | -48.5801 | 2024-10-08 00:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7263586d-1365-3659-8709-28b8e68495dd | -2.9797 | -49.5342 | 2024-10-08 00:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| eb599235-95f7-30c9-849a-66b454e8a08e | -14.2656 | -44.588402 | 2024-10-08 00:05:24 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ad722d0-47fc-38e9-990f-8153b89e6876 | -3.2862 | -47.133 | 2024-10-08 00:05:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5d61e8b3-c3cd-3edc-ac83-b45edbf8d35e | -3.2863 | -47.1111 | 2024-10-08 00:05:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 1ae80807-82ea-3f5c-9720-1e8437e41dec | -14.1089 | -44.0163 | 2024-10-08 00:05:25 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e522044-9d81-3024-b96f-2667690ff602 | -14.1109 | -44.076302 | 2024-10-08 00:05:25 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38f70329-03bb-395a-a5ee-2dcf3ae22290 | -14.1129 | -44.085999 | 2024-10-08 00:05:25 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aaa6cc8d-9c9f-38ce-9f0a-b9a6d37acf07 | -14.1418 | -44.379002 | 2024-10-08 00:05:26 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05f4354b-939d-3a11-9800-208110012325 | -14.1439 | -44.389099 | 2024-10-08 00:05:26 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f36a95c-0f0e-3b70-b0af-7c808c052733 | -13.7296 | -42.435902 | 2024-10-08 00:05:26 | METOP-B | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3d3095b3-b920-38d3-ac1c-9aeba4da051a | -13.7313 | -42.443802 | 2024-10-08 00:05:26 | METOP-B | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5f5d10aa-9432-3e30-a8d1-224ee01ef988 | -14.1232 | -44.488899 | 2024-10-08 00:05:26 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a80bb60d-ce63-3384-a2cc-c82eb86b7bc2 | -4.0962 | -48.2523 | 2024-10-08 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 059fe58e-b964-38b7-89e3-2c9e12dd6f87 | -13.9519 | -44.5998 | 2024-10-08 00:05:29 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ba79367-1352-334f-b4f4-6b02e5b0e0b1 | -13.954 | -44.6101 | 2024-10-08 00:05:29 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82aa567a-7b8a-391d-b3dc-874a98533479 | -13.94 | -44.591499 | 2024-10-08 00:05:30 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f706c514-d900-3c64-9008-5b551dba508a | -13.9421 | -44.601898 | 2024-10-08 00:05:30 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4667c37-2ca1-3228-81cc-63b1909a6e74 | -13.9163 | -44.575001 | 2024-10-08 00:05:30 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16381bb8-6ff0-3be4-b6a2-424da525a708 | -13.9184 | -44.5853 | 2024-10-08 00:05:30 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a669a87b-7fc7-3422-903f-50a02cf9ece2 | -13.9204 | -44.5956 | 2024-10-08 00:05:30 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1ae8bb1-d672-344e-a503-3f3d351cf580 | -13.4698 | -42.467701 | 2024-10-08 00:05:30 | METOP-B | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7e26cc07-61b2-3032-9035-098691f03269 | -13.4715 | -42.4757 | 2024-10-08 00:05:30 | METOP-B | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0c77128f-d4af-32d2-a3bd-52e07032b2c9 | -13.7644 | -43.979698 | 2024-10-08 00:05:30 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae9180a3-c385-3897-8a29-ea49a404a9fb | -13.7664 | -43.989201 | 2024-10-08 00:05:30 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c60f418-0537-3bf3-a460-0b0edca997d2 | -4.4468 | -42.9123 | 2024-10-08 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 47b060d5-5238-37f4-8ea5-358c1ecab637 | -4.447 | -42.8889 | 2024-10-08 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| b5af27d7-f459-3702-a718-fa26e6b8f2c2 | -4.4655 | -42.9112 | 2024-10-08 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 5f40d4b4-5310-35e7-a904-147e7568c56b | -4.4657 | -42.8877 | 2024-10-08 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| cdedd44a-4a68-3b49-95ef-0faffd1044a4 | -13.5367 | -43.175499 | 2024-10-08 00:05:31 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c6cd63b3-a8d7-37c0-8ca0-a6015d48b8ea | -13.7566 | -43.991299 | 2024-10-08 00:05:31 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b82baf42-e779-3046-91b3-88580d8c34ca | -14.0599 | -45.495602 | 2024-10-08 00:05:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 804e2e62-db66-3da0-8a28-34884a7f9d4c | -13.5893 | -43.773899 | 2024-10-08 00:05:33 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c343f4da-d037-331a-a9a0-cb3b5d439749 | -13.2946 | -42.415199 | 2024-10-08 00:05:33 | METOP-B | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 88527135-7ae2-32fe-9394-004081984488 | -13.2963 | -42.423 | 2024-10-08 00:05:33 | METOP-B | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9470327b-07e7-346a-a670-0e03ebc2787a | -13.5795 | -43.776001 | 2024-10-08 00:05:33 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3d499b0-10de-33a8-afdf-ed5d58614cd2 | -13.4809 | -43.645199 | 2024-10-08 00:05:34 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 868116ae-4bb2-3823-9d60-d8c519b75ccf | -13.5334 | -43.999199 | 2024-10-08 00:05:34 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3722ae28-6e12-3b47-a803-f119dd7c88e6 | -13.5354 | -44.008598 | 2024-10-08 00:05:34 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9dea121-26a6-3c4d-a6d2-d88481d5c94f | -5.015 | -49.5999 | 2024-10-08 00:05:35 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 1ff57a66-1a81-3871-8451-0aaa1cc34b3a | -13.1413 | -42.465199 | 2024-10-08 00:05:35 | METOP-B | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| efcccf66-b80b-3f5c-a9f5-161e44a87156 | -14.1726 | -47.326099 | 2024-10-08 00:05:35 | METOP-B | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1ac9166c-3027-3f10-8b1b-4924f8679b63 | -14.1599 | -47.312401 | 2024-10-08 00:05:35 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9f810713-0a29-348a-ad15-1200ceae40f6 | -14.1629 | -47.327999 | 2024-10-08 00:05:35 | METOP-B | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5a85a2e3-d8c7-3a4c-b956-aa4512306380 | -13.4156 | -43.725201 | 2024-10-08 00:05:35 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3090e25b-71ab-3e3d-b484-c8e4889ce880 | -13.4152 | -43.7728 | 2024-10-08 00:05:35 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46f538db-d2c3-388f-ba09-fd223a7fa7d1 | -13.4171 | -43.781898 | 2024-10-08 00:05:35 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 681f4d61-02de-301a-8a31-1d6c1b87c610 | -13.419 | -43.791 | 2024-10-08 00:05:35 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72406d03-241d-37bc-bcba-de1ce05f3d9a | -13.3802 | -43.751801 | 2024-10-08 00:05:36 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6928504-f689-3f5b-97ad-0faa85e2d7c2 | -13.3685 | -43.744801 | 2024-10-08 00:05:36 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7c12641-84b1-3b8e-a4c4-caeb6ae3f8e9 | -13.3704 | -43.753899 | 2024-10-08 00:05:36 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd22f43-79c4-3805-969b-43cf2fdf8636 | -5.4653 | -48.9141 | 2024-10-08 00:05:37 | GOES-16 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 8773a031-143f-384d-8065-a700a9198462 | -5.4654 | -48.8926 | 2024-10-08 00:05:37 | GOES-16 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2d37525d-1bd5-33d3-9f1c-6492386c982f | -13.1505 | -43.091099 | 2024-10-08 00:05:37 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aa22a0a9-266c-3a56-9457-3ed7668753cd | -13.1522 | -43.0994 | 2024-10-08 00:05:37 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b522a839-864c-375c-9189-df7abe65cab6 | -5.5716 | -44.8927 | 2024-10-08 00:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ff569852-4cc5-394e-83f6-b5ae2593461f | -5.5718 | -44.87 | 2024-10-08 00:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| be6a2097-2dbc-3140-b1f2-6f07072a5890 | -5.8216 | -44.1196 | 2024-10-08 00:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 69c20fa7-fda5-31c3-8d77-867c245ee159 | -5.9225 | -45.3888 | 2024-10-08 00:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| daece68a-1981-3382-a787-7285ddbbf6f9 | -6.4213 | -38.8347 | 2024-10-08 00:05:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 152.9 |
| 6e9fd133-46e9-32d8-b0aa-535aaf5375ef | -6.4402 | -38.8327 | 2024-10-08 00:05:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 050d3f56-ac45-367c-bc80-d16a039d16f7 | -12.5785 | -42.280102 | 2024-10-08 00:05:44 | METOP-B | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README3.md)
