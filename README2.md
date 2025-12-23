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
| be789b3d-8356-37f3-81af-63ff5c158229 | -1.49806 | -45.91721 | 2025-12-23 04:14:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 86c751c8-2ee1-3a7b-9bb2-52b0635a3730 | -1.49361 | -45.92109 | 2025-12-23 04:14:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 52b4c911-905f-38a3-bded-a4b936fbd96d | -1.49876 | -45.91274 | 2025-12-23 04:14:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11ecdc3a-ac76-3862-ab9e-eb5a3beefcb8 | -1.5018 | -45.91778 | 2025-12-23 04:14:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c50a78a7-a00e-34c5-8c8c-8eac9e1c7325 | -1.49432 | -45.91661 | 2025-12-23 04:14:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 06c77037-62ce-3dce-844f-f8eccd6797af | -1.53321 | -45.79106 | 2025-12-23 04:14:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c431781b-0966-3c66-a580-0584740e7c55 | -1.49735 | -45.92168 | 2025-12-23 04:14:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 137a47dc-e3d3-3713-9ccd-ee74a17b3010 | -1.52951 | -45.79047 | 2025-12-23 04:14:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a81c200-bb5d-33ad-a75d-8d5411ca06ed | -4.13888 | -38.49194 | 2025-12-23 04:14:00 | NOAA-20 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 15b3d93d-0f18-3506-bdcb-038d652757cc | -3.95728 | -38.39113 | 2025-12-23 04:14:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3e6ca181-2c0a-3d6c-afa8-1f4a86b3b76a | -15.0737 | -43.11242 | 2025-12-23 04:16:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31ee0fbb-b753-386e-98e9-63a2b2292080 | -13.6618 | -44.3016 | 2025-12-23 04:16:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7af691b3-f313-38ed-a2ca-55a992910a6c | -14.09467 | -46.58751 | 2025-12-23 04:16:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d649326c-26de-3785-830f-23b1ae248fa4 | -12.27846 | -43.54966 | 2025-12-23 04:16:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06a825d0-f865-3826-a2f6-385cb7d1d8c7 | -13.2945 | -43.95668 | 2025-12-23 04:16:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0c2f5bf-9c56-3e65-99c5-f737c8625f32 | -12.27456 | -43.55272 | 2025-12-23 04:16:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73a50180-6564-3ac2-89d2-67dc990db68b | -12.2779 | -43.55325 | 2025-12-23 04:16:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c170a219-7cd9-38b3-a92f-f32ed7ea13f2 | -11.14953 | -43.32495 | 2025-12-23 04:16:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9587d0fe-6005-39ee-a466-9f968e1f9c4f | -16.24788 | -42.22965 | 2025-12-23 04:16:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ae3965e3-7cfa-3fb1-afce-117851dd4312 | -12.28125 | -43.55378 | 2025-12-23 04:16:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 002f4a6a-b668-383b-a6a9-d38b888313b7 | -12.27122 | -43.55219 | 2025-12-23 04:16:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a45a151-e28c-39e3-80bc-acdc0aa037b5 | -15.58641 | -41.76738 | 2025-12-23 04:16:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4d38f7c5-71df-3edf-bf0c-a44c93eca5be | -12.2818 | -43.55019 | 2025-12-23 04:16:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cddf1462-61d3-398d-9f31-b12ebbe1183d | -16.07028 | -44.76472 | 2025-12-23 04:16:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3522c89d-f800-38cc-b323-05b4dca40127 | -14.63346 | -44.22574 | 2025-12-23 04:16:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f6578648-0a3e-3f03-804e-793c3797aa93 | -12.27511 | -43.54913 | 2025-12-23 04:16:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da4edaf8-d5aa-3241-afdc-dee48e4fd5c9 | -21.02233 | -48.66893 | 2025-12-23 04:18:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0298f5dc-106c-321d-a818-9cfbcdd27c07 | -21.4928 | -48.65031 | 2025-12-23 04:18:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9241da5f-616e-38f3-85cd-ab628fc26836 | -20.85498 | -49.09279 | 2025-12-23 04:18:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f99fa0b3-638a-3e33-94aa-6783ab863748 | -21.04804 | -49.59114 | 2025-12-23 04:18:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 535e6be8-9484-36ea-b3c0-14faafc7b92a | -22.02004 | -48.29563 | 2025-12-23 04:18:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa973ac6-503f-3efa-bdb3-1ee0502ec8bc | -21.04527 | -49.58614 | 2025-12-23 04:18:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9c1247e6-6d97-3aea-9ddd-dd4c67929c10 | -19.59784 | -46.28188 | 2025-12-23 04:18:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35b20ad3-6898-3a20-a451-8ca443c641c1 | -21.81123 | -44.94067 | 2025-12-23 04:18:00 | NOAA-20 | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2f177f7a-a2d0-3190-bbb7-e538e8a652e5 | -21.01825 | -48.67221 | 2025-12-23 04:18:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 87f95751-0695-3eaa-b651-7be20d39fc80 | -21.04451 | -49.59042 | 2025-12-23 04:18:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| efdc73b1-6283-3196-9c08-82662d440363 | -20.85428 | -49.09687 | 2025-12-23 04:18:00 | NOAA-20 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5d1c37b-a9d0-365e-987e-8fc8628df134 | -17.31071 | -44.92994 | 2025-12-23 04:18:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb70fe68-8043-370e-b96c-4d4a446a5c91 | -19.26579 | -49.18659 | 2025-12-23 04:18:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c95ea38c-5b1a-37c4-8657-0d5fc1aa7295 | -21.49554 | -48.65491 | 2025-12-23 04:18:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fc87f7f-48f7-3f49-97d5-0b2b6ebd6ef5 | -21.02166 | -48.67287 | 2025-12-23 04:18:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e7202bf6-8cba-308f-b60a-b7ae2d95ea39 | -21.18607 | -48.69871 | 2025-12-23 04:18:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2552d523-40dc-3c53-91b9-5d218ac6d94a | -19.52659 | -48.77003 | 2025-12-23 04:18:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 74b75911-1ca5-3a29-bdbc-3f9bb10c421b | -21.32974 | -48.53445 | 2025-12-23 04:18:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 121d403a-b259-37fb-9e29-54e094b436f9 | -20.87487 | -50.07491 | 2025-12-23 04:18:00 | NOAA-20 | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b3c08031-8306-3ef7-b55d-1979a05b53e3 | -21.4996 | -48.65165 | 2025-12-23 04:18:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c0a8fe0-dcee-374a-9e90-6cf96f2de80b | -19.00062 | -48.83407 | 2025-12-23 04:18:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c50f66ce-d945-31c9-933f-d4b2778a8e97 | -21.4962 | -48.65097 | 2025-12-23 04:18:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08e87c6c-cd75-3210-a6e6-007098132b8d | -21.04098 | -49.58973 | 2025-12-23 04:18:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d5afc9b1-20d8-36cf-8be3-d84badc49004 | -19.59713 | -44.12394 | 2025-12-23 04:18:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b2632d3-12d2-3442-9b62-76dcef32719d | -20.68745 | -48.79912 | 2025-12-23 04:18:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0724dc6d-8ce4-3507-8963-bfa4bf5b52da | -22.0187 | -48.29613 | 2025-12-23 04:18:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e230b47-4258-3b9b-8173-5bfdf509f15f | -20.85775 | -49.09755 | 2025-12-23 04:18:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ef4b36f-b007-3cf6-9b83-1a375bd3fb08 | -21.49686 | -48.64702 | 2025-12-23 04:18:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d8d9ed1-cc1d-3e6c-a8fc-6483744bc4fe | -20.69089 | -48.79979 | 2025-12-23 04:18:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8b0c7d0c-6cd7-328c-bc7c-3088d21cf69e | -19.60116 | -46.28246 | 2025-12-23 04:18:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c25e7a07-d525-38d6-af92-097a38a57084 | -21.37971 | -48.63311 | 2025-12-23 04:18:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e62d2093-927e-321c-a7b4-ff9f58af1b09 | -19.95139 | -44.70707 | 2025-12-23 04:18:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61badc39-5cbe-3f0d-bbc6-d497ca0bf4a5 | -20.68677 | -48.80312 | 2025-12-23 04:18:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0189fe40-0609-3a11-b856-493ba834bc5a | -25.59992 | -50.26576 | 2025-12-23 04:21:00 | NOAA-20 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6fc14b02-349c-3239-afff-7fe1125d3162 | -22.98248 | -48.64982 | 2025-12-23 04:21:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42f27323-65fa-3b04-836b-da85f78e5572 | -22.9865 | -48.64658 | 2025-12-23 04:21:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aad995ae-a861-31cb-8b02-0bcfa4444fb5 | -22.97911 | -48.64917 | 2025-12-23 04:21:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 39c7175c-d04b-38b9-b244-0355d8a26670 | -23.44819 | -48.93092 | 2025-12-23 04:21:00 | NOAA-20 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4bbe51a4-87ba-37f3-8111-2737e930dd1f | -21.9462 | -50.49784 | 2025-12-23 04:21:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a2cfbc98-0fbd-362d-b776-bf45af6749ae | -26.43477 | -51.04104 | 2025-12-23 04:21:00 | NOAA-20 | MATOS COSTA | SANTA CATARINA | Brasil | 4210704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 36bda699-7918-3ba2-a46f-90e9d8b667b0 | -23.60702 | -46.37983 | 2025-12-23 04:21:00 | NOAA-20 | FERRAZ DE VASCONCELOS | SÃO PAULO | Brasil | 3515707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4a2515f0-3ab0-3134-81b4-6e8a6153bc16 | -23.38444 | -46.41621 | 2025-12-23 04:21:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 37bed00a-d566-3539-aa4b-cdb909f620b6 | -26.95586 | -52.25683 | 2025-12-23 04:21:00 | NOAA-20 | XAVANTINA | SANTA CATARINA | Brasil | 4219606 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 50e362b9-d608-3341-88b6-184b99869023 | -24.12529 | -46.71112 | 2025-12-23 04:21:00 | NOAA-20 | MONGAGUÁ | SÃO PAULO | Brasil | 3531100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dc54292e-8d93-34de-9954-c52bb86b19bf | -25.59647 | -50.26503 | 2025-12-23 04:21:00 | NOAA-20 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b13a0084-10b6-3fe4-8cc4-2c674e9337a1 | -22.47727 | -48.35251 | 2025-12-23 04:21:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94fa7fc1-1c2f-34cc-a606-2e21f643ea50 | -9.7254 | -60.2071 | 2025-12-23 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| bf3ea818-9fce-3579-b5c9-b24e030dd084 | -9.7254 | -60.2071 | 2025-12-23 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 5b327541-b766-395a-b238-9017475fa7d1 | -9.7254 | -60.2071 | 2025-12-23 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 7e9660c3-ad5d-358a-a77d-70f6354806fb | 3.97668 | -59.95524 | 2025-12-23 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dd40d88-da47-3679-be7b-ebc167c5fb15 | 3.98042 | -59.95001 | 2025-12-23 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d2c826b-cd57-32ec-81a7-27bcf2db64d9 | 4.0084 | -59.98551 | 2025-12-23 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6c4db68-23d4-3a5a-a858-c22d9cf3a831 | 0.68102 | -59.55778 | 2025-12-23 05:03:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49c3f4ea-596c-3f02-becf-8de460777e02 | 0.68044 | -59.55412 | 2025-12-23 05:03:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c9dd49b-62ff-3c65-bdbc-ae10ebe3692e | 0.91696 | -59.78881 | 2025-12-23 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 318191a4-fdc0-397b-985e-555b3d5f4d44 | -9.72019 | -60.20153 | 2025-12-23 05:05:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de8cccaa-b872-384d-b694-9a4de571e90a | -9.7208 | -60.20242 | 2025-12-23 05:05:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 620b07cf-6ed7-3ce2-8128-3ca9a49e5c62 | -20.85626 | -49.09188 | 2025-12-23 05:08:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fce14d0e-b0bc-3e0c-bc7e-39daee667174 | -19.26699 | -49.18702 | 2025-12-23 05:08:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 250e275b-30e5-366d-96c4-7f53b57a4915 | -21.49441 | -48.64697 | 2025-12-23 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87a5b5e3-e2f1-363e-9471-6fc707ff3cc9 | -21.49404 | -48.65101 | 2025-12-23 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97392afe-e95a-3ba5-a105-8cd2a7bd71ea | -20.87805 | -50.07747 | 2025-12-23 05:08:00 | NOAA-21 | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ebd2fde-1f14-3e77-a32b-f0da1223ad87 | -21.49977 | -48.65153 | 2025-12-23 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 63116ccc-d97d-33e4-a5cf-124194970439 | -19.2698 | -49.18875 | 2025-12-23 05:08:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3fe384a-83c1-31e9-bc2e-84cea3a00983 | -20.8793 | -50.07667 | 2025-12-23 05:08:00 | NOAA-21 | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4d7f29e-e870-3c11-8695-450e0d882ee9 | -21.0205 | -48.67383 | 2025-12-23 05:08:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 15d64eb3-5303-3562-a846-f1ecbed96416 | -20.8784 | -50.0742 | 2025-12-23 05:08:00 | NOAA-21 | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9bca8e6f-8a3d-3c6d-90e3-e12e5d7a268c | -21.50014 | -48.64751 | 2025-12-23 05:08:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| badaff31-14e2-3989-8ab4-1d231fe4c403 | -20.85592 | -49.09568 | 2025-12-23 05:08:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 871461bf-fa90-3110-94f6-b1555452bb84 | -21.02339 | -48.66708 | 2025-12-23 05:08:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0a84c683-5d21-33cb-b8f6-02cf48ba5114 | -20.68989 | -48.80214 | 2025-12-23 05:08:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 351a3eb1-188c-3757-83fc-53b33d8a1248 | -20.85599 | -49.09449 | 2025-12-23 05:08:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f5c5aa2-f173-3cd5-bf42-6df34527a4e1 | -21.02659 | -48.67036 | 2025-12-23 05:08:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c262451a-1430-3bb6-9a6e-c0d3f862dada | -19.26441 | -49.18812 | 2025-12-23 05:08:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README3.md)
