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

## Dados Diários - Página 239

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31f5d1f7-ab77-3e15-8b59-379876c1ea89 | -9.9801 | -45.9009 | 2026-10-09 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| f192127b-e634-38eb-b8bc-cdfa29665021 | -11.5801 | -43.6492 | 2026-10-09 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 46319cfe-6149-3933-81dc-005c76c4f385 | -12.0063 | -43.4402 | 2026-10-09 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 391.3 |
| fc0d5f95-8e28-3941-87bb-eff9ffa5ac67 | -11.8499 | -43.5835 | 2026-10-09 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 3ee614c7-008f-301b-9722-3cc4416228bf | -8.969 | -45.1313 | 2026-10-09 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| fea85e57-6d5b-3668-938e-22a2351a3f58 | -9.0826 | -45.1186 | 2026-10-09 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| f7346749-b1dc-3f2b-8022-c930f74164d1 | -12.2145 | -44.6291 | 2026-10-09 13:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 7130964f-75c4-3c54-9f0a-17601ee5c879 | -11.2475 | -46.3058 | 2026-10-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 434295ea-5820-30f5-83e8-366e585f4406 | -11.245 | -45.3037 | 2026-10-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 69d6f52e-f0da-3888-9161-afd48cd83818 | -12.0058 | -43.464 | 2026-10-09 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 543.0 |
| 11923098-971c-3a45-8058-9c9a0c2dd092 | -11.1242 | -45.6865 | 2026-10-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 91fd2ba6-336b-3e1c-b724-5f5230cea0d8 | -10.5087 | -47.3401 | 2026-10-09 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 1ccb0165-0de6-3e68-8d73-e6daeb9cb5d9 | -9.1012 | -45.1393 | 2026-10-09 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 06c200a3-24ca-320c-9b15-cf6300da3e19 | -10.7475 | -46.6184 | 2026-10-09 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 9852bdf9-ffb6-3c25-9ceb-22d40b3ac22f | -11.6754 | -43.6817 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 0db67518-c1ed-393c-9c39-1ef0eb2beb11 | -9.1012 | -45.1393 | 2026-10-09 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 121ec918-3c77-3b46-b872-f8a0bdb4d78c | -11.5998 | -43.6226 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 9576b8c6-fa93-317b-9e18-6138c384e6d0 | -11.5993 | -43.6462 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 751d5855-3267-3cce-a7bd-f2cc4a33f14d | -10.5091 | -47.3179 | 2026-10-09 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 3eb4c181-598d-369b-acbf-04837e1af3f1 | -11.6177 | -43.6906 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| c4d844e7-dfd9-3046-9870-a7060c209d03 | -11.8302 | -43.6103 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 70f146dc-f723-3923-9e24-b4649e61bbfc | -10.8909 | -44.8001 | 2026-10-09 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 20f91368-b9dd-3f5d-8f75-6da4ed9c3be7 | -8.0766 | -45.6112 | 2026-10-09 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| e77893d7-b029-37d2-80da-1ca3c9a3b338 | -11.1242 | -45.6865 | 2026-10-09 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 346.0 |
| 4dccde2a-c61a-34ce-b8b1-0402ae202fce | -12.2156 | -57.1087 | 2026-10-09 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 137.1 |
| c5d146c6-6815-3f15-8d63-9e20d9ffd91d | -11.2259 | -45.3064 | 2026-10-09 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| ab925c9a-558d-319a-9722-8dc1ed69ee6b | -7.7022 | -45.4663 | 2026-10-09 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 6c1d9774-0909-3202-a25c-dc1f9c8aab7b | -10.4901 | -47.3201 | 2026-10-09 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 160.4 |
| dc701292-7a21-3497-b14f-b33e700faf65 | -10.9536 | -50.6805 | 2026-10-09 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| fee786ac-a3eb-3e6d-9a2a-8466f79d456b | -10.4334 | -47.3046 | 2026-10-09 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| a987da56-a0ba-3d71-85c1-a3aff14c1758 | -11.075 | -44.0768 | 2026-10-09 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 49e3fabb-982d-3d67-b90c-4f30d2897732 | -11.1051 | -45.689 | 2026-10-09 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| a4c8850d-a024-3a7c-9f9a-e537c81594a1 | -11.47 | -43.3824 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| b7de8e13-a455-38f3-b711-31ff2a268e25 | -18.3335 | -42.3598 | 2026-10-09 13:40:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.9 |
| 52e4176b-2176-3051-9588-5bb8343cab45 | -11.9861 | -43.4908 | 2026-10-09 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 760.2 |
| e217be87-dd67-3d27-af7f-be485bff6c96 | -15.3838 | -41.878 | 2026-10-09 13:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| 25b1bfdd-4762-3303-a475-9b9c779ae502 | -14.0048 | -48.7522 | 2026-10-09 13:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a4770922-2efc-3899-a1f2-f6f9e69a5da7 | -18.0688 | -44.6019 | 2026-10-09 13:40:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 277807e0-aaf5-30f9-8060-c10979a4e662 | -12.0058 | -43.464 | 2026-10-09 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 452.0 |
| d0b957d4-cc84-30ac-94c1-1cca158e0620 | -10.8789 | -45.5368 | 2026-10-09 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 23519fca-7119-349f-a492-af4a3cc37975 | -9.183 | -43.3688 | 2026-10-09 13:40:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 234.0 |
| 92fb0958-e2e7-3467-ad34-09478cc2c49a | -12.2346 | -57.1071 | 2026-10-09 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 383.1 |
| 6abdd3bb-f35f-3ee8-a382-c6a435a5a57d | -11.8499 | -43.5835 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 225.4 |
| f9c60ec4-2d7e-3c08-be61-82e43255ae1e | -8.3234 | -45.4506 | 2026-10-09 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 8a02f23e-abd1-33cb-a91b-ea911ecd5e73 | -11.6566 | -43.661 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| aa70c6b3-a190-3caa-94c5-2736828007b6 | -11.1054 | -45.6662 | 2026-10-09 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| b5a3fc68-9e1f-38cd-940c-ba9752d89775 | -14.0238 | -48.7714 | 2026-10-09 13:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 94440624-37c8-3e08-a0c4-bc8c82694406 | -9.0826 | -45.1186 | 2026-10-09 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 3c0c3f6c-2940-3d11-aec9-8e699cbe4b0f | -12.0054 | -43.4878 | 2026-10-09 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 3fb949a5-7d8e-3579-af2d-5065c1b62fa5 | -8.5315 | -46.8887 | 2026-10-09 13:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 65b363b0-609c-312d-b8a7-e3c280780b14 | -16.6321 | -47.203 | 2026-10-09 13:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 182.3 |
| eeb28f07-5b13-3107-a4da-475cba7e6c2e | -10.7479 | -46.5959 | 2026-10-09 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 5fbfbfe0-9258-3587-a595-f969b8ed63cb | -9.0829 | -45.0957 | 2026-10-09 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 30a9eeb3-8843-3ddb-9456-655177101326 | -11.0754 | -44.0534 | 2026-10-09 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 207.2 |
| fce3d3e6-19ad-38fb-baa1-b8fd8cfdbd67 | -11.0558 | -44.0796 | 2026-10-09 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 339.2 |
| a1cf292b-1bbb-3543-9753-5d0060e10e0a | -9.9018 | -44.7917 | 2026-10-09 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| f54ad686-0e2b-3c38-a827-8661f3940b56 | -11.5801 | -43.6492 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 77d79338-bdae-3593-996e-621b181ff87f | -9.1297 | -45.8179 | 2026-10-09 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.5 |
| d79c4aef-8d27-33e4-8897-debdd9ae39bd | -9.1015 | -45.1164 | 2026-10-09 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 169.5 |
| b07e70f9-f408-31b1-88e1-56e143859914 | -10.5087 | -47.3401 | 2026-10-09 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e097078e-0f13-3d75-aed3-e56626c1e050 | -9.8629 | -47.4809 | 2026-10-09 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1d813b12-1e9d-392c-abe1-e57227950139 | -10.4917 | -47.2087 | 2026-10-09 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 7d8e98a7-80c1-3c67-a77f-f72297c89d21 | -11.8495 | -43.6072 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| cc55f0a2-d3a0-3b2f-be55-6943bcfc1ad7 | -8.0575 | -45.6357 | 2026-10-09 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 09810890-1a09-305c-b1b8-219d0ea3219a | -11.6562 | -43.6846 | 2026-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 489.9 |
| 56812d3d-b09d-3576-8aa4-f575e8a1197a | -12.2154 | -57.1287 | 2026-10-09 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 1b82999d-6779-3b74-9f6e-cbc8f778075f | -8.3011 | -45.7245 | 2026-10-09 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 15d9da45-59b4-3ca6-b68c-8c51d72db540 | -12.2343 | -57.1271 | 2026-10-09 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 53010caa-b71e-3eaf-af42-2211f422d337 | -11.245 | -45.3037 | 2026-10-09 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 221.7 |
| 9475dd7f-2270-3169-843a-126a8926a17a | -11.8783 | -47.3892 | 2026-10-09 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 13c99e30-97e9-3803-96c0-c5eeeed1494f | -8.969 | -45.1313 | 2026-10-09 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 3c887d87-fe6e-39f0-a521-6d6dd23783ea | -8.9775 | -45.9023 | 2026-10-09 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 07cbbcd0-12fc-3659-97d0-180d10fb00ea | -8.9958 | -45.9454 | 2026-10-09 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 0999724d-bf13-314c-aecc-5843fd97ac44 | -8.0764 | -45.6339 | 2026-10-09 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 53aec2c9-72fb-3685-be6f-d9333db9bc11 | -14.0044 | -48.7743 | 2026-10-09 13:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 5d2a3ff1-3ab5-39b8-aabe-8f5b494627a5 | -12.0063 | -43.4402 | 2026-10-09 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 378.2 |
| 43a05bba-88e7-3145-ae2c-32497fbc50ea | -9.9208 | -44.7893 | 2026-10-09 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 225.9 |
| ee2b3da4-d9ba-3126-a402-4743de354a98 | -8.5313 | -46.911 | 2026-10-09 13:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| d04fdf71-2510-3c56-8967-2bb07ec4a36e | -10.9533 | -50.7018 | 2026-10-09 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| deaec0bb-9911-3077-84e7-a773d5f68925 | -10.5281 | -47.3156 | 2026-10-09 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 3cc18f1e-7bed-3c5f-a7fc-1c5ccc21f779 | -12.8123 | -45.5539 | 2026-10-09 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 20030681-bfdc-3a29-b472-3f344ff61937 | -11.0566 | -44.0327 | 2026-10-09 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 298.8 |
| 5ccf5568-e053-3fd1-bd43-de31bf1ca586 | -12.2154 | -57.1287 | 2026-10-09 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 861760d1-fda2-3c43-b877-dc6402ef80b6 | -8.9775 | -45.9023 | 2026-10-09 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| e5e59597-c8e0-377b-b4b6-d7b7928bf0c3 | -10.8983 | -45.5114 | 2026-10-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| ec0587fe-8b90-39c7-983f-886ab1be6309 | -12.1537 | -44.8013 | 2026-10-09 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| b9ee1992-aa9b-362d-8f50-56d3013afff6 | -8.9687 | -45.1542 | 2026-10-09 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 678bcd68-980a-34c1-ba5a-21c21f94482b | -11.6754 | -43.6817 | 2026-10-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 3bab54cf-f95a-36d6-b22d-b90907665e76 | -11.619 | -43.6196 | 2026-10-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| e6b1f31c-eb27-3ac3-a4cc-d5e8e1fe2838 | -9.183 | -43.3688 | 2026-10-09 13:50:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 240.7 |
| 85260c19-1328-3009-b781-de9ee3a08f5a | -8.5313 | -46.911 | 2026-10-09 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 64f04586-b117-3d51-9082-b82df7aac863 | -18.3335 | -42.3598 | 2026-10-09 13:50:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 180.6 |
| 24dd96d1-3032-39f6-92e1-f75b7f9ac550 | -11.6194 | -43.5959 | 2026-10-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 33560761-a008-3c86-a453-eb593689006e | -8.2176 | -46.4068 | 2026-10-09 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4f13e332-6b32-3d72-87c3-0c13df507068 | -14.0048 | -48.7522 | 2026-10-09 13:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 1cf21f9f-d826-3f85-b41a-79e0a989b0f8 | -9.8986 | -50.49 | 2026-10-09 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a8d97c04-0f13-3e43-af57-99cd7c1952d4 | -8.969 | -45.1313 | 2026-10-09 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 89ac940f-8ee1-3d3b-961f-5a3b657f5a29 | -12.0058 | -43.464 | 2026-10-09 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 411.2 |
| 38737004-f480-316f-a0db-4c0b5ceaddbc | -10.9533 | -50.7018 | 2026-10-09 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2fbf7a1d-85af-36b3-a344-38a8ad9907ad | -11.3371 | -46.6547 | 2026-10-09 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |


[Clique aqui para ver as próximas entradas](README240.md)
