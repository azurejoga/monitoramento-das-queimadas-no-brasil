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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d7ef17f-e395-360e-a589-e0c0d9599476 | -11.9539 | -51.0597 | 2025-09-09 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| da2d27b5-5d3b-3d3c-8b2e-8a4ae6840940 | -5.2265 | -43.6774 | 2025-09-09 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 9798fb80-9368-391c-a586-04b9c035a4ec | -5.8152 | -44.8298 | 2025-09-09 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ea436ac5-2dfc-311f-9556-9933fd5fffd1 | -5.9378 | -45.7704 | 2025-09-09 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 48511646-ee87-3422-89ad-b07f5e7100f6 | -5.4587 | -42.797 | 2025-09-09 14:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 4adf0d0a-0de4-3ee9-b6bd-56e4f151d89a | -11.3552 | -50.4233 | 2025-09-09 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c9066347-730f-35b0-8698-0c2fae26f9f9 | -12.6343 | -56.9725 | 2025-09-09 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 711a0c4b-7bd5-3e08-9f04-c9a246dd70b0 | -5.8582 | -44.2088 | 2025-09-09 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 214.8 |
| ad49bfe5-a1c2-3c2e-b0a2-2219086b765c | -11.9729 | -51.0575 | 2025-09-09 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| c48c44c2-1d3d-3b42-8736-7af4e90338db | -6.4096 | -45.3067 | 2025-09-09 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| fb776358-0d50-3cce-8b30-4d4f479aeb4a | -9.3394 | -65.4638 | 2025-09-09 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 3ddc3418-8d46-3661-bcbf-49c5fbbc05bb | -12.529 | -45.2756 | 2025-09-09 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 226.3 |
| 8909db1f-9f49-3424-869f-0ae75c0a5f0e | -9.0232 | -49.7834 | 2025-09-09 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| fc2ede18-6790-39e1-9497-dc08da29b0e3 | -11.4281 | -43.578 | 2025-09-09 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 663461c8-d613-32d2-923d-fbb12e2bb68a | -20.0883 | -47.3502 | 2025-09-09 14:40:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 6500e926-cff7-360d-be92-43191bdbbf15 | -11.9726 | -51.0788 | 2025-09-09 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 05d6b4a8-3007-361e-834a-8445e7654071 | -19.9545 | -49.2928 | 2025-09-09 14:40:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.2 |
| aba9c85e-3a1f-36c1-957e-5c2286051c37 | -5.6015 | -48.1082 | 2025-09-09 14:40:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 7fc84bd1-0178-3f3e-a8a4-85b2b94379a1 | -5.6418 | -45.4312 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 4d57f70c-5de6-3063-b510-040ed60c1ed7 | -11.3011 | -46.5244 | 2025-09-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 9d83dae0-e04f-3e63-9c9b-882cb8563542 | -13.054 | -56.8545 | 2025-09-09 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 42876710-f881-35f7-be98-40c3a41f9660 | -15.8397 | -52.2631 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| feac63f5-05ad-31d1-85c8-14f461055950 | -17.2973 | -46.6799 | 2025-09-09 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 1935ed54-782f-3183-84d4-b22f1ad70fe8 | -6.1803 | -45.82 | 2025-09-09 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| b49ec9c7-716e-33e8-a6c3-3e66b3c9c589 | -12.18 | -53.8836 | 2025-09-09 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 6bb8ce11-231a-3a20-ad3a-a09a585fcee1 | -5.7483 | -43.9406 | 2025-09-09 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| fa9e7d44-d384-3dc9-8cf3-0aa1db4b6b96 | -5.898 | -43.9523 | 2025-09-09 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 725329a1-cf25-33b3-a4d5-50aa3e0fde8f | -12.9482 | -54.7519 | 2025-09-09 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 533.3 |
| 7f9c314a-1e26-300d-8f30-81c75e6d3c30 | -7.881 | -46.2598 | 2025-09-09 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 6f07723f-07ea-3be0-bd41-6b7ae0ba5458 | -5.453 | -43.4525 | 2025-09-09 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 7102fdf3-eeda-3324-a789-e2f8860b183e | -5.5504 | -45.1891 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| ef483f6e-8070-3ad0-bb4c-8ff4d570a496 | -14.3231 | -47.3171 | 2025-09-09 14:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| e578dfe8-bf63-34d5-a333-e0046bf3e2ba | -6.2407 | -43.4144 | 2025-09-09 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 949ea1b2-ed62-3773-98ec-e7669888ff3a | -7.1825 | -44.9006 | 2025-09-09 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 5e4fdcb6-f6d1-334e-af1b-c92d5b8fcf25 | -15.8205 | -52.2444 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 150.9 |
| a966bc9f-53bf-3888-a686-e0ff4840d98b | -5.5506 | -45.1664 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 63024ece-7c53-39a3-803d-87e8584b3bc3 | -5.6603 | -45.4525 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| aeae1d35-cad3-3125-8b0e-be9b572a578d | -11.1061 | -51.9958 | 2025-09-09 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 0080533a-8238-3829-9c03-3f6772338066 | -5.8397 | -44.1872 | 2025-09-09 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a5f9f5b8-9998-3065-bfb5-81be8b9ec31f | -12.5286 | -45.2987 | 2025-09-09 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| c52f3271-fd26-34af-a287-ba65f86bba5f | -5.6925 | -43.8986 | 2025-09-09 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 3c971390-be74-3e4a-9dc3-6155c1f56512 | -16.3602 | -43.0349 | 2025-09-09 14:40:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 829302c9-182f-3766-8b7f-76542424e3af | -9.6289 | -48.0129 | 2025-09-09 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 2f4f8904-f15c-349d-9e19-49f4123acda4 | -14.5601 | -52.2262 | 2025-09-09 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5adcebe3-071e-3834-8ce3-6ff32a8ba0f5 | -5.9191 | -45.7717 | 2025-09-09 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |


