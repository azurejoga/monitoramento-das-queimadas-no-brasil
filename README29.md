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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 897c5385-5089-3966-ad9e-dad62821e92d | -5.61528 | -45.00603 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f2601a0b-2e6a-34c4-9dcc-80a944e040ce | -6.17118 | -44.07717 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c7529d9-1117-34ad-962f-a62a40fec995 | -4.6742 | -41.02009 | 2025-08-29 03:49:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b2002eee-a8b5-3501-9903-e3ed7c721cde | -13.6681 | -46.91648 | 2025-08-29 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f26cdcee-2a2c-3c3c-8d5a-f0a8af02d1c0 | -13.67417 | -44.22004 | 2025-08-29 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9debe896-37ab-32f9-a894-eb1670778a01 | -11.55819 | -46.36067 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0daba632-c8e9-3961-a435-df17ce1edab5 | -6.53518 | -43.10365 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a942503-00c2-3c71-8dab-9d6da2171344 | -14.24708 | -48.06734 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf1ab1b4-580f-307d-80a7-48f743beb4a0 | -7.56208 | -37.18981 | 2025-08-29 03:49:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 434cf43c-90c0-36cb-ab40-0a1a5601a03b | -5.62189 | -44.99799 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 139aa2df-431f-3a05-9364-b7cbe03f707e | -11.60887 | -46.20116 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c172dac-ed90-3d43-859b-3c5d74654599 | -13.50832 | -46.93975 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b65a0b7f-0e6a-3447-b885-085f5d54ea2b | -12.08627 | -44.72315 | 2025-08-29 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6786553f-5c53-3aa3-8988-a8798f3ba6c4 | -17.54071 | -46.61627 | 2025-08-29 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 556912df-97d0-399d-bda4-54ed5c2b4c9e | -10.83608 | -47.47889 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32af4e0b-65a7-3c4c-b46a-2f61539241ee | -5.85857 | -42.93715 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1ff847cb-e6d1-3a9c-a62e-2f7f9bade983 | -4.08343 | -48.04342 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ab0559f-7fb5-3791-9233-8f13a83d0da2 | -11.32956 | -43.57063 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eacfe48-0b2c-3788-9029-1d52a7274cd4 | -11.89978 | -46.71597 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41a9a867-50e2-3270-9fdb-eca73a037704 | -13.51452 | -46.85503 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3217f43b-4fca-31d4-9344-22903f3731bd | -12.83644 | -48.1738 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4338d6fd-d9d2-398a-b1cb-4e30b9029ae2 | -12.32067 | -47.04692 | 2025-08-29 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e998114b-3147-3567-aa68-267c9e577200 | -6.21968 | -43.37051 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38b8b01f-eb01-3406-8db4-48d68113cd41 | -6.34879 | -44.47708 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f65fdbe-5ab9-309c-8c94-625b2fefdb9e | -11.59071 | -46.38004 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22be3af5-d4a2-32b0-bf50-ed7a80c3bd1b | -11.29057 | -43.5409 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdafe9d6-fea2-3ddc-9054-bcf074ab67fb | -10.85408 | -44.79776 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a1f83fe-ec77-3418-8bda-1ef083452efc | -13.53587 | -46.87807 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f5d5c79b-1ec4-3468-82b3-01c13c32e99c | -13.45409 | -46.95516 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee3fe4d3-695f-36a0-9723-403e976d9259 | -13.50119 | -46.84402 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ac373632-4fbd-3672-960e-5ca26ea37a10 | -5.98384 | -42.97346 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 379beb50-d13d-3891-a439-9fcfe09b99d1 | -10.94222 | -46.86242 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a64dd15-874b-3161-81d5-25a276d5ad55 | -4.09519 | -48.20248 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 689ed712-4718-3dc2-bf28-569faf526c6d | -11.31912 | -43.55696 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49171713-8197-33e1-af4d-77ee768bef49 | -12.92314 | -46.34894 | 2025-08-29 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c5b84c3d-67da-3864-a7e2-e6d9a2776345 | -6.30028 | -42.49384 | 2025-08-29 03:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 54fa7cb0-9d8a-3de7-9924-1517f8c19125 | -12.70157 | -48.19286 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b2d42aed-396a-3f66-adb4-e09700de782e | -13.5348 | -46.88359 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1d563c5d-d881-3823-a60a-51813cc214c5 | -12.91481 | -48.12237 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 853db067-ac6a-31ff-be8f-c5c119113555 | -12.83083 | -48.17337 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3592588-d35a-39b5-930e-d144f9f74105 | -17.53978 | -46.62112 | 2025-08-29 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c015fe0e-a876-3234-a1e1-07c9bab0a53f | -11.06784 | -44.76052 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd985a69-5316-331c-9dce-758a8f0328a5 | -6.26707 | -43.81542 | 2025-08-29 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 784f46f9-1971-3a45-90d4-695d5a110772 | -12.81341 | -48.1749 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ac83705-7538-3731-9534-56344e0bb921 | -11.08712 | -45.12621 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8730ba8-5c8d-3f17-bfcc-e42d263ca5c7 | -5.61567 | -45.01137 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b20ec02-6ef1-3dab-9b6d-fb2d97400922 | -11.35225 | -43.53936 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0f18452-704a-3738-84d4-ede6cdf361e9 | -13.54887 | -46.94485 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fdc2a398-9a7c-3e15-abd0-0ec43101ced5 | -15.78749 | -43.34895 | 2025-08-29 03:49:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2adc05fe-04e8-3d3e-a515-f6bd6eaaffa7 | -5.6158 | -45.00305 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 838d0eaf-f80e-38a6-8d4d-5321528ca754 | -11.23405 | -44.12992 | 2025-08-29 03:49:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f6f6c0-29de-3c3f-8a8c-63abc0fc2fe2 | -13.49613 | -46.84309 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28a4c7e7-dd05-340d-b294-70ccf6c3245d | -5.62273 | -45.00031 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a6854386-4ae2-3443-87ef-5ff5622a2eb9 | -10.02066 | -48.07543 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15faf9c3-25f5-3dd8-91e0-61ccb9226e1c | -12.83163 | -48.17019 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8b6715e-ddee-34fc-8846-4c57cf7ef916 | -13.97783 | -46.32783 | 2025-08-29 03:49:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8954cd9c-00b4-3607-8ba1-3520c6c9a265 | -11.56051 | -47.62035 | 2025-08-29 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af42bdba-86df-35c0-b194-35419d0e358a | -17.75746 | -44.47997 | 2025-08-29 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63337c52-e4cc-3f08-89e3-d209277189eb | -15.17013 | -52.3312 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db514222-4bb1-34e7-9b50-877d74b3214b | -11.32752 | -43.58207 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f158c95-eb05-3cbc-8182-12c1b269f6a1 | -12.92656 | -48.14963 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d54934e0-0fe7-3085-be8c-94ad07a4d1df | -13.61457 | -48.24572 | 2025-08-29 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ef0e2f5-b3c1-3b6d-9576-edd589e7c6c9 | -13.41669 | -46.98719 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f4256202-1b93-3206-826b-d3d47dbe40d1 | -16.07986 | -43.62659 | 2025-08-29 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad31383b-ad14-3c2d-8f98-15cb68460e8e | -11.2899 | -43.54474 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67aa0b62-8a7b-392d-b6f7-977c5ddec410 | -11.83232 | -46.79422 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd14be85-f0f7-3603-8abb-2579ce588858 | -15.04064 | -48.13568 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac92ac7e-e2d8-3697-9fca-82cb6a811ed1 | -6.22252 | -43.36947 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22676d51-bc8f-315a-8bbd-39226e282116 | -11.57587 | -46.37648 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be24ef8e-07d9-38a9-ac73-37319a0a9ef0 | -12.80876 | -48.16964 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7048cdab-6b55-3f8e-bee2-9313b8242110 | -12.83302 | -48.1624 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 733758b3-6a3a-3dd6-9461-01c18da58b96 | -12.87097 | -48.14325 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e60ed7e-243d-34cf-a2a1-0562b3c1f07c | -5.61475 | -45.009 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e75ec703-def9-3ad7-8bff-28dced72c1a8 | -11.02669 | -45.07228 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce05ea3d-c350-3874-93ba-69dd6dd2ab97 | -17.34935 | -42.64436 | 2025-08-29 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fba1d3e7-6efc-3e26-acd4-141d86625982 | -11.07917 | -44.7553 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 196ce7e8-eff9-369d-b288-448064967fc7 | -12.80804 | -48.17437 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33781382-b5b2-33e2-a7d4-0b7a72f13b16 | -11.55964 | -46.38024 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ca4daff-1e52-3557-8b61-ba5c574058cc | -16.45405 | -40.55679 | 2025-08-29 03:49:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bbb8fcae-8d0d-38fc-8bf4-a958a8d5d9a1 | -12.81606 | -48.19186 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b710a44-d5dd-345d-a03c-efcc1b39294f | -12.81115 | -48.18615 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7737954-b1ca-3681-81db-36d3d84a0da6 | -12.45007 | -47.99501 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c13b94a6-0f84-317d-b31d-907874e02087 | -14.84561 | -46.75218 | 2025-08-29 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32acaefb-3983-365b-a330-af1298451ac8 | -13.50881 | -46.93726 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51ab44c9-16f5-3ed8-a1cb-a9b6a0bece93 | -13.33413 | -40.34556 | 2025-08-29 03:49:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0ddb7114-d3cf-3884-af21-0ae3154ddd33 | -11.88142 | -46.39856 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eaab5de8-7a4c-3889-84b0-69d11f324fd6 | -6.43504 | -44.57563 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9391ec2-5478-39e5-8dc7-1370d9735e73 | -13.54082 | -46.8792 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f0a0d414-9236-365d-87f9-a4cd40128544 | -10.8314 | -47.5034 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0eafc90-b61a-3fcd-82c3-2b7a37855cec | -6.20031 | -44.13386 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaccef05-7bad-344e-9348-c6df7f8936c8 | -11.3453 | -43.5302 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 789b4fa3-2464-3c09-81dd-189880a6147e | -12.83941 | -48.10005 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2647f13f-8220-3e9e-b4d0-f595cb461a18 | -11.09443 | -44.74844 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46296442-f6d5-348c-83b0-831c0421e868 | -13.5616 | -46.90557 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ffe0ae3-49b8-3e9e-b298-8be5ed5cb50f | -15.07537 | -48.126 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60fff5f2-e9ae-3b97-8c2e-36d5e785e81c | -13.43322 | -46.95552 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 034c91f5-6d31-3a9d-953e-88faeea40c98 | -6.56122 | -43.69334 | 2025-08-29 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dfb5ad7d-52c3-3a13-9622-edc5663a8c4f | -11.5596 | -46.35328 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d49faae2-e2b4-3838-9fb9-3565b7d23078 | -5.60023 | -45.21041 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0920455e-9755-334b-b746-2a5740a5b3c6 | -13.4999 | -46.85042 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README30.md)
