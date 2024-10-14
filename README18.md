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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c671ac5-3bd9-3c47-8396-47b241bcd882 | -10.90763 | -44.69651 | 2024-10-14 01:17:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 75d7419a-7d2f-302e-baed-1daa3dba5256 | -10.90751 | -44.69096 | 2024-10-14 01:17:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 65ac0995-f77c-351f-aaf8-1a7494df720f | -10.49443 | -42.45878 | 2024-10-14 01:17:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 92.4 |
| f057c5b0-fdaf-3739-9421-ed40d8c5e263 | -10.49399 | -42.46374 | 2024-10-14 01:17:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 5fcf6034-6616-3d6a-8805-53a1e20ebd16 | -10.4866 | -42.41589 | 2024-10-14 01:17:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 592638db-c409-3b50-92ad-afb0914f343a | -10.48648 | -42.42096 | 2024-10-14 01:17:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| d0f3ed18-0a40-3855-b361-2d92365ce12a | -10.43079 | -44.9517 | 2024-10-14 01:17:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 47.1 |
| ef10f9e0-b4bf-396d-94e8-7aee2d413e24 | -10.11844 | -43.94243 | 2024-10-14 01:17:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 5a0c0c5b-da6d-36df-beff-cf68ce5bb77c | -10.10938 | -43.9508 | 2024-10-14 01:17:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| bad29826-911d-3d31-8202-dca10e68cace | -10.08517 | -44.25496 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 6e976225-1d6c-3f30-ae89-ff165b6764ac | -10.08027 | -44.25048 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| c37dda74-e030-3b52-9c6c-588f4febb138 | -10.08004 | -44.22419 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 7dd422dd-20d5-36d8-b9d3-2e9e54b9ea38 | -10.07491 | -44.21981 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 193.4 |
| fc9def99-1f2e-3522-919b-abecb0da628d | -10.07485 | -44.1931 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 41.3 |
| fcd28f4e-2a99-3a5a-aad1-0e42067f1113 | -10.06972 | -44.25787 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c3772e9a-5d10-3516-a18d-d0430f2df935 | -10.06947 | -44.18865 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| ccb99cbc-ae52-3a4d-9583-ff54f35d9989 | -10.06486 | -44.25358 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 1dc2f1ef-1022-3d08-b246-8a1a9438673c | -10.06457 | -44.2272 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f82b66c6-e4e3-37d2-a13b-ae17c2b2760b | -10.05945 | -44.22282 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 44.4 |
| a2a702bf-958b-357a-8a3d-aba6a63f6141 | -10.05929 | -44.1958 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 21ed7161-058d-39cf-abf2-cc8a693f4027 | -10.04911 | -44.23026 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 506d8252-5fe7-366f-8089-3182f6fdbdb6 | -10.04375 | -44.1986 | 2024-10-14 01:17:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 79ec5877-bd23-334a-8f1a-378f7f348f97 | -9.88353 | -52.28648 | 2024-10-14 01:17:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b5c86ae4-5c0c-3ee8-b8e1-ac4352d59b55 | -9.88222 | -52.27733 | 2024-10-14 01:17:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 76f2414e-56da-3737-bc6e-b2174ba90631 | -9.70892 | -47.46876 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 17bf6978-378d-3ca0-8347-842cda928320 | -9.7038 | -47.48216 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 288ba34f-0829-35b2-817a-19ddd6bb688e | -9.70096 | -47.46463 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7612bbfe-5533-3e1e-95ec-91ed64541710 | -9.69951 | -47.48825 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 3b80e162-2766-3dab-898b-2cbe02296c78 | -9.69678 | -47.47061 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 87d7568e-677c-37fd-b1dc-cd2266cadff1 | -9.64391 | -51.77481 | 2024-10-14 01:17:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6e0f8ae8-65b4-3f50-98b5-2b0c9ae99aae | -9.61874 | -48.9897 | 2024-10-14 01:17:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6fa36a36-e13c-3786-ade1-89151f3c4070 | -9.56598 | -47.6946 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 58410e06-5c11-3133-979b-947ef73b8012 | -9.56062 | -47.70124 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3d4e7876-6844-3144-bb64-fcea90dc2f36 | -9.53548 | -47.6172 | 2024-10-14 01:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 388e9887-261f-3b47-a6af-60a4cfd73919 | -9.47679 | -45.84481 | 2024-10-14 01:17:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 46aff3eb-f27f-34d1-8d51-d3330d770b46 | -9.47292 | -45.82124 | 2024-10-14 01:17:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 7fe390a6-5d73-3774-8d39-c5b9f3c5922f | -9.297 | -48.24801 | 2024-10-14 01:17:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fe1b7100-2742-3472-a561-8cb3b230aff6 | -9.10137 | -47.94489 | 2024-10-14 01:17:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| fde3d1a9-e0da-3931-8757-a091b1c46b4c | -9.09882 | -47.92834 | 2024-10-14 01:17:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| b1ecfa8e-a92b-348c-bb09-d96485d55907 | -9.08959 | -47.94683 | 2024-10-14 01:17:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 1933e3f7-9e0e-3b9e-a76d-c84459fda796 | -9.08703 | -47.93038 | 2024-10-14 01:17:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 903d452b-1fe8-341a-a1b8-c0f128d7083a | -21.7593 | -48.3086 | 2024-10-14 01:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 6ba39e94-62c7-3cc5-9071-9cb9ac4522a0 | -21.76 | -48.2851 | 2024-10-14 01:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 0d1b9cea-7229-3233-9520-a527f1fc26f8 | -21.7808 | -48.2801 | 2024-10-14 01:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 09a13be9-a995-37fd-b335-c2c8869985a0 | -21.733999 | -48.2589 | 2024-10-14 01:19:03 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8d22fcd8-900d-30b3-9ace-bf66aea60405 | -21.739 | -48.2771 | 2024-10-14 01:19:03 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8dc0435f-cbd0-3c94-9a51-9f7d67074ef7 | -21.743999 | -48.2953 | 2024-10-14 01:19:03 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 687f8927-861e-3984-b190-39db4f860917 | -22.2852 | -49.098801 | 2024-10-14 01:19:06 | METOP-B | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 85b6f8ee-3890-342e-950c-667d79408217 | -22.2756 | -49.101799 | 2024-10-14 01:19:06 | METOP-B | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ae568d7a-9ca6-335b-aa91-a77902874712 | -21.7437 | -48.255798 | 2024-10-14 01:19:11 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8fe57323-e010-301e-aa48-837cc054232d | -21.748699 | -48.273998 | 2024-10-14 01:19:11 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 147d36b3-9256-34a0-a3bc-0867e4fd0e03 | -21.753599 | -48.292198 | 2024-10-14 01:19:11 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ab0875f2-6791-359c-b67e-be0655e0aa23 | -3.21535 | -48.91439 | 2024-10-14 01:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 15cccb03-3cf3-3633-bc09-27c693402222 | -3.19616 | -50.31393 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| f1c7e215-7a58-319e-9aa9-f2f9db966c71 | -3.19419 | -50.30022 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| cb1d7de4-96d0-39db-9486-dd31f426a3b3 | -3.18531 | -50.31551 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fd6b7d3d-968e-3be6-b0dd-4bba6702d09d | -3.17456 | -50.46868 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| b22b9cb7-7e5d-337f-81e0-929418dcaee3 | -3.16384 | -50.47028 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| b2e1875b-6605-308a-943d-c71d7ae03529 | -3.12832 | -53.7399 | 2024-10-14 01:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c8ca188-edd8-32c4-a43d-57f7698ad1d2 | -3.1194 | -53.74118 | 2024-10-14 01:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e3ad9667-2f69-3f09-8c87-8efbc5421024 | -3.11814 | -53.73218 | 2024-10-14 01:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dc48b814-06dc-3aa7-a5a9-0a9748072eba | -3.1058 | -53.05168 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b0ab9417-3276-32fe-87ab-5293f70f5546 | -3.10447 | -53.04222 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8418a59b-3154-3b92-a13c-b709c7d00339 | -3.10313 | -53.03271 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a97c6802-923b-3a04-8a95-ed44fa0e7f03 | -3.09666 | -53.05291 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 55124ef8-e508-3ffe-9a2e-29c91643c239 | -3.09533 | -53.04347 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1a31970a-f53a-31c8-a0c3-3a45d27f6d52 | -3.09399 | -53.034 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7fbe2962-71ff-36fe-986e-ead75d5a248b | -3.08484 | -53.03526 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4d46c76-ba16-3db7-8d56-c0d57e313807 | -3.07946 | -54.243 | 2024-10-14 01:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 24af876d-550c-320a-ae39-85812bba99b6 | -3.07704 | -51.1945 | 2024-10-14 01:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| f56ff1fd-e96e-34d6-a0a4-923bd2cc035a | -3.07648 | -51.20085 | 2024-10-14 01:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ac74154c-c387-35e7-8438-fd76567a8d6b | -3.07537 | -51.18255 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 4002b79c-8095-3e7f-bf44-cc52b71c630d | -3.07473 | -51.18894 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| d8b199af-d9d7-3459-9a7f-dfb573d0f1f5 | -3.0737 | -51.1706 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| b8aaa6bf-ab3a-38c9-bb09-0d6b111ccd76 | -3.07297 | -51.177 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 39eb5596-6cda-30e0-860d-5bf92abe0570 | -3.07061 | -54.24424 | 2024-10-14 01:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4003cf2a-b6b9-35bc-b97b-d3f85db2e06e | -3.06686 | -51.19596 | 2024-10-14 01:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| da81fc06-743b-3717-b6f2-d5d7f132ae06 | -3.06525 | -53.88274 | 2024-10-14 01:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1c753539-b8a0-33b7-877a-b9273764a3ca | -3.06518 | -51.18401 | 2024-10-14 01:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 5fcb227c-d17b-3bbb-929d-2d55111fc350 | -3.06164 | -49.37892 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ebe7e03d-64f1-31be-a316-6d3ef011dbdd | -3.00456 | -53.44836 | 2024-10-14 01:20:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ec179a4b-6343-345d-9196-8d104c212f72 | -2.96198 | -54.65752 | 2024-10-14 01:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 7b72fd5d-e7cb-3ff7-ac86-ce3465acdeda | -2.96075 | -54.64874 | 2024-10-14 01:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 76fe20d6-d6df-3bd6-8cf0-5ba8e329eb19 | -2.87718 | -48.91024 | 2024-10-14 01:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c74b0036-9d24-3fce-a2ee-e32d939fb69f | -2.80762 | -54.08337 | 2024-10-14 01:20:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 54f80484-d086-3594-a102-86677965db43 | -2.7934 | -49.29677 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 22222178-ddb2-3912-82b2-6672c055f3df | -2.78733 | -49.30344 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 13ee2d10-271b-3392-a55a-b7f25c8e2ea5 | -2.78495 | -49.2868 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 92c43639-1fb9-392e-bdbe-0e3ebc83e5f8 | -2.78026 | -49.42159 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ccaf25c1-afb3-3422-9380-f7ae37212cb4 | -2.74985 | -48.40331 | 2024-10-14 01:20:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 769c13e0-14f1-324d-92e1-828ab21a98a8 | -2.65572 | -54.31573 | 2024-10-14 01:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c30c219e-b362-3ca8-a5f3-f59c12f7256d | -2.65449 | -54.3069 | 2024-10-14 01:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c9fa6cdc-e833-392a-84fa-7e1da442b0b2 | -2.63512 | -51.75828 | 2024-10-14 01:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 17a0270b-e7f0-3099-8fb7-b1fae56ab62a | -2.62084 | -49.12748 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| eedee383-5cb7-305e-b5ce-505e5bfbc6f3 | -2.61831 | -49.11034 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 3d28ee90-42d2-3069-baf6-2ab8f3ea30a5 | -2.61788 | -57.5707 | 2024-10-14 01:20:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 80a8ca5b-eabc-3f69-95cc-4271c6bd8387 | -2.61577 | -49.09308 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 23466389-5efb-3a95-a7b7-321d1b08e77f | -2.61321 | -49.07571 | 2024-10-14 01:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 08780b2d-2ca9-3622-afc9-7588bb4c33d1 | -2.60816 | -57.57205 | 2024-10-14 01:20:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 0eb324d4-7cd6-381e-b202-53a066564f60 | -2.60669 | -57.56128 | 2024-10-14 01:20:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |


[Clique aqui para ver as próximas entradas](README19.md)
