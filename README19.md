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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 698d6edb-8687-316a-b41f-469bd5bc82d2 | -12.37794 | -43.78005 | 2025-11-17 03:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de724bff-0338-3cd7-b89a-64000ac0cf22 | -9.75225 | -43.96296 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2aee8794-7efb-338c-8f88-ce03af5e7602 | -8.53413 | -46.07858 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97f4321d-7edf-38ce-af71-dd108b6b4156 | -9.72159 | -43.95702 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 56e4598d-28ef-30af-a4d2-53999454b5ae | -7.97233 | -50.01068 | 2025-11-17 03:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 327299fd-967a-3ef5-9f34-bab8a0fe29d4 | -11.81931 | -47.5862 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1068a1c1-61e8-3d9d-bcc8-5d6f9de19680 | -14.85611 | -47.37672 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6335ddf6-acac-38d7-8225-704c14b9ba46 | -10.91071 | -49.41697 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4261d270-e1f1-33b3-b919-aea5fc74794e | -9.73244 | -43.97259 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2042bba9-6e92-33af-a130-8071f04fbd27 | -14.55541 | -42.71191 | 2025-11-17 03:49:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d8f52079-33f5-377f-bfba-2adcf4a3cac3 | -9.79755 | -48.56654 | 2025-11-17 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b5642f7-bc03-3e9b-8491-5106b58dfccb | -12.85501 | -46.46482 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39f2d132-8e39-317d-9bb8-74a38b49771d | -11.99665 | -49.27852 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 708f2bc9-45b3-37e1-b7c6-4ffbd67c501f | -3.62276 | -44.44212 | 2025-11-17 03:49:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9196521-0d12-3371-8e12-5dc88eed04ab | -12.02418 | -47.01355 | 2025-11-17 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39ef0b15-0653-3cfe-a6fe-65f7ec92114f | -10.78701 | -44.32341 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67bdcd18-e25a-3a52-9a7c-0a01ade5c812 | -9.51289 | -47.2711 | 2025-11-17 03:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42bc987c-fffb-33ac-a8f7-fac4959bb5f1 | -9.65153 | -43.91879 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c8a2ac35-527f-3ab4-b07e-f45fb233dfdd | -11.81522 | -47.58828 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d52d7b66-ec98-3e7a-8bb8-7ba8a4410b62 | -12.80085 | -46.44613 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cccbc62d-598e-3599-9bbd-d9d87c8ed9dc | -9.65302 | -43.91022 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ec4d7ab8-2184-328e-a451-f48b503794ac | -12.67034 | -47.18158 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a68a07ce-b414-31fa-b07b-48a57bf572f6 | -10.96744 | -44.53548 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 190fdb45-3bca-3e67-affd-88d5288f7a50 | -10.84974 | -46.75447 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fceb6e0-be22-3bb5-af73-f732ea200dcb | -14.64479 | -46.55208 | 2025-11-17 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50e0e1b8-536d-3d4b-9ea7-07df1b0dd903 | -3.4791 | -44.74212 | 2025-11-17 03:49:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 923ec5d2-c6ea-3cfd-ac26-aa00047f5b61 | -3.22108 | -43.36126 | 2025-11-17 03:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| defa9a2b-fa33-379e-b62e-db458e068e5e | -8.90184 | -41.02966 | 2025-11-17 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1197665f-1091-3c3e-843e-5af0ce5fe251 | -9.79522 | -48.56215 | 2025-11-17 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6147463-89f2-3131-bcd0-d9ed85ef7c4f | -12.50793 | -47.26268 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19280ced-919e-319b-baf1-cbccb3bf8737 | -14.88456 | -47.36456 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c89f0b52-6e00-3faf-9a53-4c48093e41a2 | -9.15117 | -48.06773 | 2025-11-17 03:49:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f773f27c-804f-3658-b36d-ed7fafac5560 | -11.15829 | -49.44548 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a97c089-34a5-34b9-a6e5-7ee579fa35c5 | -2.51774 | -47.83122 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f4a680b1-19b2-31b3-9216-4804a5db6437 | -12.66172 | -47.16384 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f323ebf1-3b32-321c-9e81-8906c177ba32 | -12.66113 | -47.16698 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69d72333-dba7-365d-95b4-fa78b2da2cfe | -11.81402 | -47.58462 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d329d245-3894-3121-9bad-6cb7034c47fa | -10.31375 | -44.2906 | 2025-11-17 03:49:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cef0d617-7831-39e8-8c03-f12b470f2a32 | -10.78312 | -44.3241 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b614be22-0218-3b2b-8fdf-6540fa2bfc94 | -8.53804 | -46.06491 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15c78c32-f23c-35f3-a67b-3c6cfe8b2d83 | -14.65072 | -46.54708 | 2025-11-17 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9978840c-6c7b-3c5d-8b43-7614780dd517 | -8.30452 | -43.94255 | 2025-11-17 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e369e122-f145-3f40-862d-92b9e8e5ad3c | -13.27745 | -47.29673 | 2025-11-17 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ecf1655-0c92-3992-9c67-84334556aec8 | -9.31958 | -46.57544 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d22d8b23-39e7-3159-a25c-111193a55ecf | -8.29811 | -44.19363 | 2025-11-17 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 162b3bf3-4f66-3741-bf0c-4738571857ae | -9.58222 | -49.12151 | 2025-11-17 03:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ecc99477-4d93-3f57-8a18-aa75867da710 | -10.96761 | -44.52351 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4caa3d08-9b48-3c5e-811a-4c22e36b76ee | -3.66869 | -44.82374 | 2025-11-17 03:49:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c59f7ae0-ed1b-334b-9a23-4958499424e4 | -2.52008 | -47.82744 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| dc1b5af8-002d-33c9-9a23-ae2c167d1122 | -12.43127 | -43.17399 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c0693621-ed12-3001-a2e9-035f0a1fcaf3 | -11.3418 | -48.91187 | 2025-11-17 03:49:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3863bf5a-37e2-3cdb-94ca-04076d828340 | -14.58533 | -45.22768 | 2025-11-17 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd222e57-9f76-387d-ab90-73c51dffb05f | -4.85391 | -39.04988 | 2025-11-17 03:49:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9eb22e33-7c82-349a-aeb3-ca283a3983db | -8.0515 | -45.66323 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f190e08a-4f94-3a23-b8d7-3efc559809b5 | -9.74636 | -43.97078 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0fdd7bd-ae8c-3f7b-bd32-26d1e1dac4d9 | -3.62859 | -44.1928 | 2025-11-17 03:49:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edabbe44-973b-3189-8b68-5b55bd8e8edc | -11.40548 | -43.32091 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 596adbdb-d9b6-3e8c-b5ba-349a24170441 | -12.66053 | -47.17013 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e02af1c-0aae-3c2d-8b25-f3c94ebf90bb | -8.57849 | -45.67985 | 2025-11-17 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6741a04-4f33-34c7-9a52-24b81f44a85f | -10.85466 | -44.87851 | 2025-11-17 03:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e75ed097-1d5b-3ad8-9880-64eead5a0ab6 | -8.32277 | -45.41122 | 2025-11-17 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5f0be07-c093-3bb6-a3a2-05ddd353e325 | -10.92662 | -48.68412 | 2025-11-17 03:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eefd9900-2dc3-31bc-90ac-bb41befaabf5 | -11.05467 | -45.1573 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e550a451-38a5-3f24-8f8c-80026d925b4a | -10.95428 | -48.69861 | 2025-11-17 03:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f211756e-bd44-39f7-8409-faa2224f4e67 | -14.91172 | -47.35407 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b953a8c-d71e-3074-b790-169cbfe0444a | -4.06265 | -42.08675 | 2025-11-17 03:49:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f01ea10b-dd12-3619-9696-bcd509f8057b | -14.63891 | -46.55677 | 2025-11-17 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04ddf960-87af-38d6-ac9f-9db001a3e4b2 | -10.95286 | -48.69617 | 2025-11-17 03:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d122c1d-110b-3a2f-92e7-78b6bed056ee | -10.38867 | -44.92273 | 2025-11-17 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fab26dab-93a2-3949-9703-3c1dba387c0e | -5.11337 | -39.05743 | 2025-11-17 03:49:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59c1abc6-bcf7-33d6-8d93-7c26435ca3ce | -12.40163 | -47.58789 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c32918be-4c50-3a44-9dca-11fc179d7b20 | -9.85656 | -44.1877 | 2025-11-17 03:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d495def-dabe-3879-ba77-24c4cfdd0975 | -12.42729 | -43.17323 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 287c5cf1-9a23-3f3c-8779-6a6f335065c1 | -8.32623 | -45.41763 | 2025-11-17 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3afbcf3-a897-3fbc-bd3e-986c0ddd2ee7 | -11.8159 | -47.58483 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50af8e89-ed01-306c-be39-824745473f9b | -12.70338 | -46.77462 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d68dcf5-ae04-3239-a10b-1fba1f5fe8f8 | -9.86903 | -44.19493 | 2025-11-17 03:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec17e003-0237-368b-94d1-f23746cd051a | -11.6752 | -44.72439 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c465686b-de9b-3da7-989e-ca5496e8d52d | -9.51838 | -47.27216 | 2025-11-17 03:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61ca41b1-96fe-34a8-86f8-d67a47b87136 | -14.64767 | -46.56283 | 2025-11-17 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a0e6c5c-2ecd-3b12-a53a-accdf16a9b12 | -10.65914 | -49.37388 | 2025-11-17 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 91f08590-0f7e-3c91-90e7-dabc4cd0428b | -14.88528 | -47.36083 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e616b902-8c04-356a-9586-aadc95074e80 | -12.81098 | -46.39146 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3ef8cbd-ef43-3430-9d34-836b836a1646 | -10.95203 | -48.70029 | 2025-11-17 03:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93295389-d042-3d04-8107-343d0a8832cd | -3.66316 | -44.88982 | 2025-11-17 03:49:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fb04b5b-14c1-3a84-9ae6-174f2e6ad1b5 | -12.41529 | -48.10059 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36e0457e-17cc-32de-b5e6-f04c77ca113a | -11.97411 | -43.9965 | 2025-11-17 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdbb5807-f78b-38ab-9064-58a5efe40f63 | -8.82997 | -47.36329 | 2025-11-17 03:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 665a2183-f6bd-3811-be3a-3fb244cb9e7d | -11.81982 | -47.59336 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ceb0bdab-7997-3cfb-bcee-3d4e21360e75 | -2.50912 | -47.81492 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8c1a025d-c353-3506-b30f-4ca53f76b82b | -3.83586 | -42.01569 | 2025-11-17 03:49:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f50a92cc-5ee0-3a15-9d08-b330ec4c3270 | -11.40355 | -43.33209 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5c59af03-54aa-3fc9-aad5-0631be476f60 | -12.79922 | -46.40014 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7349779-dc25-33be-9ca7-21fd0aeb2da7 | -10.6601 | -49.36898 | 2025-11-17 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 68c126c0-20cf-347f-8d1d-bcce18f3cc3c | -2.52189 | -47.81691 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| db9d1c21-4d03-3d24-9a69-924da3ba2634 | -10.84914 | -46.75766 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c403012a-ea43-3932-be21-5d179d2282b2 | -10.62991 | -44.60455 | 2025-11-17 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb98f35a-b6b9-3405-b295-31cedd2a4dfd | -11.9679 | -44.30216 | 2025-11-17 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cbdfc7a0-480f-3c4c-8a92-561bd322ed37 | -12.65596 | -47.16597 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3486d5a1-10f5-3090-b3aa-6534fabca1bf | -10.85033 | -46.75127 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README20.md)
