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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba5251a5-ed09-35b3-9c53-b3315280dc48 | -6.83867 | -44.31461 | 2025-08-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8518b696-6ae8-3da1-83cf-65c18a38ed20 | -8.3271 | -45.00782 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3679f7e5-9664-303f-8b8e-2521ee6e709d | -6.59222 | -43.39471 | 2025-08-09 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ac4adf4c-1c1a-3d01-a611-7e13a5dbfbf3 | -6.92782 | -44.6992 | 2025-08-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4b93e65-2451-3cc4-b7c5-87b8f17d620c | -6.27647 | -45.28532 | 2025-08-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fec591b-1a90-3db3-a0d3-f0750297b941 | -8.05814 | -46.32279 | 2025-08-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66244126-50cd-3ec3-8a8f-2adf4c99cee4 | -6.93973 | -46.05893 | 2025-08-09 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 033ccb31-276e-36e1-ad4f-91e85b93af98 | -3.26462 | -39.39585 | 2025-08-09 04:14:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0a1b40e1-77da-3289-b373-3481973eac35 | -5.74078 | -47.42315 | 2025-08-09 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d44fc8ef-1c8c-3dda-a060-c2a1043a3104 | -6.07246 | -44.89354 | 2025-08-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16f5b8c6-82fb-3f0c-8dd2-796c9eb8315c | -4.00658 | -47.93761 | 2025-08-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ee66be4-c520-31e0-83b6-d73ecc58657c | -6.06042 | -43.75012 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 192a2d11-9510-3999-ad91-eafc13002078 | -6.13648 | -42.96199 | 2025-08-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 89d70b4d-0d1d-37b5-8641-1bc6af314723 | -4.17196 | -48.57957 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1630fa0-027f-3d57-bfb9-d68eb8cdf504 | -9.0785 | -40.00701 | 2025-08-09 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9cbd5997-bd47-3238-a86c-51c8b9883002 | -10.44698 | -44.34211 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2a6cf20-5fa5-3705-8ec6-f5bad4c900c5 | -11.79945 | -44.93169 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c80ce00-ef98-39af-be4e-d465eb96ce2f | -16.79394 | -47.53758 | 2025-08-09 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 927bcf34-770b-376a-9e9a-94510bc46bea | -12.03972 | -47.5131 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8f23dd6-aca9-33dd-88d0-b8c28c633d7c | -11.32862 | -55.22522 | 2025-08-09 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 188a7188-643d-33e7-b329-58c6c06f71bb | -12.56237 | -47.12804 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c38d9a71-f95d-385b-9300-63e9b4e587b1 | -13.62602 | -49.01082 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ed8bc141-2f85-3e41-8838-1d6fd5fc279b | -21.73101 | -47.67955 | 2025-08-09 04:17:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32e54d46-7ad4-3a83-bac9-af71c7b12a0d | -12.65431 | -44.49028 | 2025-08-09 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b70f7f4-b2e0-3564-af90-ab4e692d5304 | -13.54958 | -55.25615 | 2025-08-09 04:17:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b23275d-dd6c-33a7-abe2-c7eaf749795e | -11.10348 | -50.47745 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9811fed-9709-3495-9813-a7e7ac394aa8 | -10.45199 | -44.39663 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81a83ff5-2777-3dc9-8f89-2b2b95d5a400 | -13.62217 | -49.01063 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 644f72d0-dd56-38c9-8221-f5f61087b682 | -15.26928 | -40.33681 | 2025-08-09 04:17:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5382dbd7-2114-3dee-8108-d06f5ec9f411 | -20.77487 | -49.21577 | 2025-08-09 04:17:00 | NOAA-21 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1b36091a-237a-3803-a65f-f959d0c73da8 | -12.49498 | -47.50756 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53d09be8-9b59-3968-b1cc-7a791771252c | -12.56287 | -47.10366 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a12917f1-023f-3f80-91ea-aed90fec71fa | -12.71593 | -47.7943 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd764a97-34eb-36fb-8066-fd98a2dfb2f2 | -12.61073 | -48.10817 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a412397-0ce6-3436-b4e5-dd18a0b217d9 | -11.32279 | -55.22403 | 2025-08-09 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2686ca5-da58-3fc7-ae3e-94115e4bad2d | -11.9343 | -44.55021 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d065ccae-0be3-362a-aab2-09ef08271189 | -11.74301 | -45.03098 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 707b39ea-561b-3428-968f-a197a5682c1f | -10.43873 | -44.35154 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9470346-a41c-3883-9da8-a9bbe5d66d6d | -13.77749 | -48.88155 | 2025-08-09 04:17:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a721f04f-ae18-3c8e-8344-7c6a318aab61 | -22.7438 | -47.38971 | 2025-08-09 04:17:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 42c24278-4c4e-3391-87b2-27420c96f7d3 | -22.14895 | -49.4539 | 2025-08-09 04:17:00 | NOAA-21 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6cd708b3-273e-3839-852b-77958cc0a5e9 | -9.96755 | -45.85539 | 2025-08-09 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf8bf0db-14e0-3e84-bcd9-13ebac43d1c3 | -16.09038 | -49.32025 | 2025-08-09 04:17:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec30a1af-8552-3b50-aa00-d06e894e51d5 | -13.63189 | -49.02197 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa6d6484-12fe-3e63-aab6-1dd1d0abc6c6 | -10.63625 | -44.76002 | 2025-08-09 04:17:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad629701-9a27-36bb-8b22-1ff41b4552b2 | -22.1856 | -47.09094 | 2025-08-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b82885ff-ae00-3160-9cd1-880752f6b055 | -13.07078 | -43.83643 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8f69c53d-2498-3b40-8d91-1b25723a9e81 | -10.44643 | -44.3456 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2687619-0ffe-3b8d-a8ac-b23980cf7268 | -11.25158 | -50.18705 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36ebe963-5411-3cd8-83e6-b8bf31b3ea05 | -13.1801 | -43.68017 | 2025-08-09 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 053c6abb-7f0e-3fad-9cb1-56965b0b10b2 | -11.72581 | -47.50044 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 818b4bef-bc4b-31b9-a3fc-be16a5e5d8f2 | -13.05272 | -56.85106 | 2025-08-09 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f7deb5d-b3f9-3cb5-9d15-f9d523a67dc0 | -15.14105 | -45.65446 | 2025-08-09 04:17:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64b92a8e-f415-3b64-8f54-f9ab7a527d56 | -13.9882 | -44.67765 | 2025-08-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf3fcc7e-af87-345a-9700-94d3e0746663 | -12.49144 | -47.50696 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e071d08-97c4-353b-8079-f528c1137a23 | -9.86337 | -44.69971 | 2025-08-09 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 62e0f486-d901-3676-b4f4-cec1d0a1a67d | -17.31133 | -40.68219 | 2025-08-09 04:17:00 | NOAA-21 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c2053b54-62a5-3a89-b575-5683f9f11431 | -11.93485 | -44.5467 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4090a17-04aa-3e11-82d0-c736b6b1d236 | -10.64247 | -45.23568 | 2025-08-09 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c6a52f6-4dc8-32a8-9790-9e6471e689ee | -14.18519 | -49.72472 | 2025-08-09 04:17:00 | NOAA-21 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06f0d52b-fbfc-3c08-8e10-0bab4be38935 | -12.688 | -48.205 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34e90bde-fe15-37cf-a5f4-f291fde1020e | -12.55369 | -47.09438 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b23badf-fc6b-320d-ab8e-fa469ae33b85 | -13.55039 | -55.25219 | 2025-08-09 04:17:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5bcc0f4-fc75-3754-8612-aed0dd588dd8 | -13.04906 | -43.84805 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7e3787c0-49ed-3ce5-a765-1bb04f8c9b94 | -11.93871 | -44.54372 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a2d66a8b-fe00-36df-b31a-498e2e19abff | -12.56783 | -47.11675 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7594217b-84cd-3cbc-ac89-1507dc35d59b | -10.00741 | -48.12947 | 2025-08-09 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 561699b8-2fb0-3ff6-946d-b8754948c201 | -14.50136 | -52.11552 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed6de902-5ca3-3087-bcfd-1f199e626101 | -11.73149 | -47.48856 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 487360a7-6992-36b0-b2f2-96f5b6f9697d | -11.0904 | -50.50071 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69913213-0c21-3aad-af5d-b05cb25510bf | -12.68434 | -48.20439 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9ba1256-739c-3be3-ae93-48a2e59a7bfc | -14.16371 | -43.66575 | 2025-08-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6f2f5659-9fcf-3477-aa17-2eb011e6acab | -9.86392 | -44.69619 | 2025-08-09 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 78e2e168-ab1e-3745-a2c7-b3138ad98720 | -12.58995 | -47.17752 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07320c93-c20a-3290-bdb8-f0c00acc0799 | -10.17908 | -49.51053 | 2025-08-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 699545c6-9b0a-3b02-9e32-ffe1d839246f | -14.11549 | -45.40709 | 2025-08-09 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7c36904-08d2-3e0c-b538-cd20acdf990b | -12.59409 | -47.17418 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6370cee-f58a-36d3-b8bf-772a9cda9f52 | -10.1798 | -49.51088 | 2025-08-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c925faf-6b66-3ec9-8b08-38beb8db58be | -9.01377 | -51.11327 | 2025-08-09 04:17:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd598104-6024-38ff-932e-55cb6ae45d88 | -13.55213 | -55.25751 | 2025-08-09 04:17:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9d6a220-ee33-32a5-b08e-89ca6b502fb9 | -13.06798 | -43.83231 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0c0a9526-b50d-3a2d-af49-5f4098f67118 | -15.7642 | -48.04829 | 2025-08-09 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7192221-7989-3570-ba70-a6f1e19823c1 | -22.14618 | -49.44912 | 2025-08-09 04:17:00 | NOAA-21 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bd49997e-5894-3b5d-a09f-7ec4ac32c42e | -11.08965 | -50.50485 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e5e75fe-cd1d-3cf4-b4e2-7c0e940f6b34 | -11.7308 | -47.49268 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49913b4d-a169-3908-b81d-a03b1e2f3af7 | -10.57987 | -44.79417 | 2025-08-09 04:17:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8be6c84-c01d-32f8-976b-3fdef33047c6 | -20.10508 | -45.28347 | 2025-08-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ae2e0b32-5a8f-3a94-a52c-b643968eb37a | -11.74938 | -47.49132 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5796d7e9-169b-35b6-af2f-2534400934f2 | -16.46723 | -42.51387 | 2025-08-09 04:17:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b72fc67-68fa-37dd-9246-7fc496369394 | -10.43487 | -44.35451 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dd8b624-bd00-3fb7-9cbb-fd243fb96f77 | -14.65602 | -49.73265 | 2025-08-09 04:17:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9237c10-a7b7-33a2-b28d-341caec51ed6 | -14.45698 | -52.07791 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6721d2a2-6f6a-3c78-aed3-0b99bec77c46 | -19.81244 | -47.06169 | 2025-08-09 04:17:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ae07738a-47d3-3cb6-ac32-8f2f556242a9 | -10.44753 | -44.33862 | 2025-08-09 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cd3f8a0-7129-3c7e-ae00-dfe4f4bd3b3b | -13.05239 | -43.84858 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96be3a08-b712-3cee-8708-2f0ec033eb1f | -14.96755 | -49.55358 | 2025-08-09 04:17:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb5b6de7-7f81-370b-b2ba-0d7d346d20f7 | -13.07132 | -43.83283 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2b3f9ec5-8c6b-31fb-b3ce-781f8e2ab5cd | -12.56717 | -47.12074 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f294035b-d74b-36b0-85de-ea9f35589a28 | -13.04572 | -43.84751 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dab37988-8c93-377b-aa42-444daac105cd | -9.99989 | -48.12806 | 2025-08-09 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README14.md)
