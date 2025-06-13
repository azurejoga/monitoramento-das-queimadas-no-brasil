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
| 84f3a16f-6c06-3ab2-90dc-0b675842bf8d | -22.77173 | -49.3186 | 2025-06-13 04:14:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd74681b-134b-307e-8c8b-582410492605 | -19.6999 | -54.61529 | 2025-06-13 04:14:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb4097a7-5b3c-31c7-b9b0-e5da255fa404 | -20.09356 | -50.86631 | 2025-06-13 04:14:00 | NPP-375D | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f52dbcd3-09a8-3a6b-98bb-af22c373df14 | -21.3493 | -48.5914 | 2025-06-13 04:14:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7787497f-35e6-3159-9dd8-def3c114e86d | -23.33876 | -46.77493 | 2025-06-13 04:14:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bcffad27-85e4-3618-81c5-eedf40b6819d | -21.1943 | -50.66008 | 2025-06-13 04:14:00 | NPP-375D | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0d1d428e-76d8-3c31-be4e-ecf035d97177 | -23.23607 | -51.28705 | 2025-06-13 04:14:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b92094c2-d561-3fa8-8464-a254840d8e59 | -20.09414 | -50.86785 | 2025-06-13 04:14:00 | NPP-375D | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f9e2059c-0b24-3045-90f8-ae096aa0ac67 | -23.59436 | -47.44113 | 2025-06-13 04:14:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| db9ae451-93ae-31bf-910d-7aa782c56705 | -22.92293 | -45.41325 | 2025-06-13 04:14:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 28d67e2b-0cc5-389b-80bc-92ed72cb237a | -21.34566 | -48.59064 | 2025-06-13 04:14:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e1fd32e8-f730-34dc-9ba0-cc89ef84ff64 | -21.34849 | -48.59595 | 2025-06-13 04:14:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e795c1a5-f2b5-37d3-ad54-f4d5914bba76 | -22.7726 | -49.31393 | 2025-06-13 04:14:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78635537-d713-37c1-a8fa-2af7d54a3b01 | -23.63025 | -46.42635 | 2025-06-13 04:14:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e38ea2f5-19cc-36ea-978c-06d7b05c6dc2 | -22.10588 | -47.01386 | 2025-06-13 04:14:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bddf033-0710-386a-ac8d-dfbb7efe0c98 | -22.10521 | -47.0178 | 2025-06-13 04:14:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 388f1ad0-777b-36b3-a719-17e91c23fcd6 | -22.77012 | -49.32003 | 2025-06-13 04:14:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4310185-a684-35cd-8d7d-7b867288c4eb | -23.3394 | -46.77109 | 2025-06-13 04:14:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 60002486-8772-3180-8089-23631e65d633 | -20.09778 | -50.86721 | 2025-06-13 04:14:00 | NPP-375D | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c8c4f5d-61b8-3a60-b98d-056573ada63a | -21.66899 | -56.63279 | 2025-06-13 04:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e82f1b46-391a-3e48-9d5a-0f3586e7f970 | -28.58822 | -49.44056 | 2025-06-13 04:17:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b2403fca-92af-32f2-ac51-c3e108ab4350 | -10.9355 | -56.8322 | 2025-06-13 04:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 98035382-e168-3a57-99aa-da6191146d82 | -13.9059 | -54.6291 | 2025-06-13 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| e3df3776-153a-35f5-bf54-fa0799dae98c | -10.6492 | -49.4267 | 2025-06-13 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ab4f9d9a-8dec-319c-b7d3-4ee59839821b | -13.8867 | -54.6312 | 2025-06-13 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8bc1dd8a-9af8-385c-999c-2338c1a350c8 | -4.19072 | -38.3719 | 2025-06-13 04:29:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 543924a2-a5d1-3a83-9929-c4aad07b5fc1 | -5.90608 | -43.45168 | 2025-06-13 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc8bb8c2-a7cc-3593-9533-7f2524429613 | -5.89968 | -43.45292 | 2025-06-13 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccf70432-8cbd-3406-9039-98ea7a630f40 | -5.90352 | -43.45349 | 2025-06-13 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 829cc7e0-d021-3f4c-a1ca-6d8c627bb8ec | -4.1912 | -38.36861 | 2025-06-13 04:29:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 814ddd9f-f8b3-309f-b3b0-d22212b00bd8 | -6.49167 | -42.84985 | 2025-06-13 04:29:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 582ebf0c-4c4f-3e76-a008-b1bc852ebd55 | -5.6039 | -44.9018 | 2025-06-13 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 280070b9-bd1f-3974-8eb8-9efc996e3ab4 | -5.90224 | -43.45111 | 2025-06-13 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2adde14e-147e-35cc-abd0-d6c99a0b4ea2 | -5.90154 | -43.45586 | 2025-06-13 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 110b86a6-63cb-33bc-bfe5-b550795ef8d2 | -5.7752 | -43.60962 | 2025-06-13 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08e30b09-22ad-342e-afb4-038e3d4e836e | -8.07 | -43.1216 | 2025-06-13 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 8dcdccf3-d461-3983-908b-2af408293ec6 | -10.9355 | -56.8322 | 2025-06-13 04:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 5444bcbc-f213-318e-a609-683d94e042d8 | -13.8867 | -54.6312 | 2025-06-13 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 932456e6-892d-36f3-b047-4b869c3f38e6 | -13.9059 | -54.6291 | 2025-06-13 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 8dd2a5bc-586c-3a46-bfe8-d0535af71927 | -10.6492 | -49.4267 | 2025-06-13 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3ce24902-5fd0-364d-a159-16dc2313fe2b | -9.84122 | -44.70813 | 2025-06-13 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7b861a90-aee8-303b-a985-940dac972b80 | -7.44961 | -45.50978 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6186370a-6d79-3ef0-92a3-1e83fdc86857 | -12.10823 | -48.87465 | 2025-06-13 04:32:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdb21a3d-8d1e-302c-89c0-2928d235eadb | -10.13535 | -47.43681 | 2025-06-13 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec4e7b6a-5b62-3921-8272-55a28df67c99 | -10.50136 | -49.02822 | 2025-06-13 04:32:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f49255e-cd8f-35d8-95d9-3acffb3fcec7 | -11.58986 | -51.33746 | 2025-06-13 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7b23f9d-41ab-385e-a898-65040e7e314c | -10.23331 | -52.23545 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7619111b-b5ef-3904-a073-b8cd583ac637 | -11.37175 | -55.11464 | 2025-06-13 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e9f35ba-83ae-3663-af61-abaf49461a3c | -7.44902 | -45.51371 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b2526622-7f64-3f04-8e03-b7d1bb05cc52 | -9.22171 | -62.47248 | 2025-06-13 04:32:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8acc61af-f3b1-3b5d-a0e7-c6527b9f2f69 | -9.41075 | -48.42696 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6bc7ea6-db6c-3a5f-a582-09a75d87452a | -10.93347 | -56.83657 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1a37b602-8e7c-3191-b22d-c81dbbee959f | -10.8718 | -54.32267 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1d9fca3-67ff-32ba-9e77-499c5c805eac | -10.6381 | -49.42793 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0b20a8de-3e40-312b-807e-49aff7696b76 | -9.88872 | -46.27803 | 2025-06-13 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e448186b-6276-3fa4-a1a3-96de26343340 | -10.64255 | -49.42144 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d4d4325a-3c81-3f52-bf93-b37474add8dd | -10.80749 | -54.04247 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3019ab84-1723-34b4-aaf1-8bf03c6555ce | -10.64959 | -44.48046 | 2025-06-13 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 06ad68f7-e205-3702-990f-38f04dd0bebf | -12.05511 | -48.07731 | 2025-06-13 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a410538-abb2-34bb-bd3f-b8671fc3a507 | -10.8627 | -54.30177 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7adef02-fbfc-3353-b737-a887aed500ed | -12.19793 | -54.26687 | 2025-06-13 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea9639c9-9992-37d9-9400-009b9b4c57f5 | -9.3909 | -48.42379 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eed2d05f-a143-317e-871a-c4d242859f7c | -10.65526 | -49.42711 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04fcdabf-3b93-376f-be31-12f4fc2fb47a | -8.95529 | -47.27611 | 2025-06-13 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b5584452-3289-34a2-9a8d-ba66de7c2194 | -7.69684 | -45.78101 | 2025-06-13 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86d83488-e69d-33d5-9354-af98ec9ffd8e | -9.41184 | -48.41999 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd055d49-9264-33b9-98b6-277be8cf28eb | -11.55944 | -54.57011 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 869d922f-2834-32e9-a417-5512d175f1ac | -11.88338 | -54.67856 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b60ffe0e-552f-30ed-9ef5-07c01b1153fa | -9.67004 | -48.7648 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31b612c5-9454-3888-b5ad-71a302cd832b | -9.39421 | -48.42432 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e9a2970-424c-3aef-81e3-adb495dbf52d | -10.86422 | -54.31743 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47c23f24-a9f2-353c-b2fc-2dc435b66bec | -10.2938 | -52.84273 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4158ba4c-ae3f-3af6-b226-8cbc0b68f5a0 | -11.56358 | -54.57087 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 83da8d7b-c7c6-34ab-82be-1b16cdcd9399 | -7.45312 | -45.51033 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cee95d6-4688-3096-a5fa-529bd5e0368c | -9.15082 | -49.03903 | 2025-06-13 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6e240fd-445b-3dc8-bd20-af79deafe102 | -12.09998 | -49.48622 | 2025-06-13 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f20fc3f-1c1e-3307-80f7-32732ba4d282 | -9.40356 | -48.40797 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2c3db75-6175-340b-8718-476447227c12 | -11.57184 | -54.57242 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2cdedaf7-b57d-3bc2-971e-2a5dc4417afa | -10.3656 | -57.22677 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aed7624-b933-3a6c-9085-f471a7233f4d | -11.93113 | -49.48027 | 2025-06-13 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ee6f035-1b7f-3fb4-933b-d09c73af85ca | -8.07406 | -43.11113 | 2025-06-13 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 5b407792-a869-3929-98de-4af77cd6a3c4 | -7.44434 | -45.52098 | 2025-06-13 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e356fe5f-d8e3-31bd-93a9-b6297e29242b | -11.78092 | -47.32201 | 2025-06-13 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a6f3175-d715-3578-8cb7-56f1c4934b6c | -10.36699 | -57.2253 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3161a718-5b9d-3c0b-9478-08f3929688be | -12.20194 | -54.26765 | 2025-06-13 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 527f416b-2987-3652-91cc-39c637b198c5 | -11.12502 | -53.94753 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 274f24cf-0649-3aae-af7e-ea57df93a4c6 | -11.74627 | -54.71853 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 751def67-4114-3032-814e-4da7975b18ae | -9.87776 | -61.39563 | 2025-06-13 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54c86df6-d3e3-3f94-9b30-45de235a919d | -10.8796 | -54.75225 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e98a1888-0e42-3eb6-8b85-d986998df10a | -10.86833 | -54.31819 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e023c184-1d4f-3ebc-8fd4-193b31b28ea7 | -9.41405 | -48.42749 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26f321cc-1364-35ce-a699-d94bfd170c68 | -10.36592 | -57.23115 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2afd3af4-eb64-3c1b-affe-f53be9cbd4b0 | -10.91992 | -56.82824 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d3739b8a-7879-3a06-859e-3b69807f7e49 | -10.64086 | -49.43198 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36767ced-91c7-3f94-9729-f30cd9a49f60 | -9.84761 | -44.69036 | 2025-06-13 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 093811b6-1c89-3e5c-bb9a-186af1883561 | -9.40499 | -57.5532 | 2025-06-13 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 23520a18-5e93-3024-9add-f1cc64aaa871 | -9.68275 | -56.98884 | 2025-06-13 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 806dd324-f1e4-351a-8e10-807a448a20eb | -7.89192 | -49.74552 | 2025-06-13 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3be81411-c853-30a6-afa2-5fdc8f09c0eb | -10.36712 | -57.49927 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0011fa0e-fcf8-337a-9ef1-92c0966cfb3c | -7.72637 | -46.61616 | 2025-06-13 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
