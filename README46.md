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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0486667-0c82-3ccb-82c2-e7c871fce1ee | -10.60904 | -42.31945 | 2025-11-14 04:46:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 538176ce-e5fe-35b5-93cb-e21e7e91f355 | -10.76009 | -45.01797 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2efae74a-738f-3277-b252-3ca7ef6bdca6 | -7.93033 | -44.32304 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b04be3c1-0cc5-3b8a-ad7d-056b70a3e9a4 | -7.93358 | -44.33321 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f62eaa3-1b14-37bf-9745-f5ee1d29b29e | -9.34459 | -46.59079 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e382b88d-4301-3d50-9473-cfdb3d6f5d4c | -7.48724 | -45.91127 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0498aa8-6f52-3e85-81fa-8bba3d4c37a3 | -9.93977 | -44.93499 | 2025-11-14 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcc8e582-690b-3740-a435-fe9d05fdf533 | -12.82531 | -43.44844 | 2025-11-14 04:46:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df85a5a8-5859-3636-8343-8f15ddf4659d | -7.92692 | -44.34683 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85f16646-8528-3171-93de-e208336819b4 | -12.21195 | -44.94783 | 2025-11-14 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fe4de9b-f968-37c1-98f0-253ce4046235 | -7.3915 | -48.65277 | 2025-11-14 04:46:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6288656f-4c30-34f0-8656-0de07806fd66 | -7.50818 | -43.01525 | 2025-11-14 04:46:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2d136747-868d-3bcb-8def-34a184974916 | -6.83959 | -48.00531 | 2025-11-14 04:46:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad95e1bb-7dce-3df2-b84e-f0aecc6c3064 | -8.94339 | -49.81215 | 2025-11-14 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2ec8f02-29d4-3caa-8c1c-38829fc4fd5a | -11.09266 | -43.17298 | 2025-11-14 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86dda416-7e5b-34e1-af08-effefbb157b0 | -13.96661 | -47.05333 | 2025-11-14 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eebd34a8-ff19-32a1-bb53-4f88afdcafb3 | -9.34983 | -46.5882 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2ec7e178-58b1-3858-b2f2-f9e67aa4b5dc | -12.07827 | -47.88561 | 2025-11-14 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a72a7285-47de-3281-9fcf-a546247a967d | -7.02002 | -46.4365 | 2025-11-14 04:46:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bef391da-76c2-3f67-973f-a8686080c6fd | -9.05865 | -44.77849 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1abd0807-f2e7-3de6-b290-32b8078db0a4 | -7.3909 | -48.65671 | 2025-11-14 04:46:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04b8f47d-c841-38fc-bd66-6b2c57afde82 | -11.74546 | -48.52647 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 166cda9a-d905-3b8b-a679-b485f70938be | -13.27384 | -44.26054 | 2025-11-14 04:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00bcf96d-4d6c-3e93-97ad-5287b9c3ee96 | -10.7559 | -45.01653 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97842b9d-5c80-3cac-b7d2-9d06883f4286 | -12.66773 | -46.74951 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80170ec2-bcb4-3fee-9c32-344292b3c88e | -11.17524 | -47.45859 | 2025-11-14 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ae46229-f3e9-3d4d-9947-220a94d3df78 | -12.68504 | -45.431 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 54d5ff68-1c76-3700-a481-dfa3a92fbbc5 | -7.06691 | -48.36156 | 2025-11-14 04:46:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0269807a-75dc-37df-8ec6-e34153325fc9 | -10.32081 | -44.27938 | 2025-11-14 04:46:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6aea469e-51e3-3d73-82e2-c3214b2045ca | -12.66299 | -46.75283 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 224df78d-93d9-3381-ba74-4ac0577faa25 | -11.85342 | -49.21463 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| f944df4f-27cf-3d4e-ad00-a15bd670b1db | -12.82572 | -43.44514 | 2025-11-14 04:46:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa49c534-be34-3daf-af45-cea0192764cf | -12.70925 | -45.42463 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c9027e1-2971-385e-bde5-e8aa8ca62792 | -10.70269 | -44.49011 | 2025-11-14 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8933a230-8282-3826-b22e-bf50c76f91fd | -9.34479 | -46.59476 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d303798-be16-3c35-9e03-6ef67ff76af8 | -11.73127 | -48.51977 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e41753e-5ad5-32fe-a13f-52679c4c1523 | -8.91027 | -41.07298 | 2025-11-14 04:46:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| de08a3ec-47e9-363d-ae42-20d8b2ef2590 | -8.96524 | -45.11496 | 2025-11-14 04:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 921a9cd6-4cf1-3e57-890b-7c9b87878d8e | -14.67548 | -46.56997 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f0e764e-e18c-32c6-8650-e6e1023f3dd1 | -12.71843 | -45.42585 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5a42f7cc-469d-3a25-b53e-e760e41f90aa | -9.02427 | -48.75845 | 2025-11-14 04:46:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43dadb7a-ca14-3e92-bbb4-319191a9f558 | -10.10582 | -40.9002 | 2025-11-14 04:46:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0ee2d84f-65da-31cc-a660-5015ce2c4b27 | -11.73153 | -44.669 | 2025-11-14 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdd655bc-3b8c-390b-8f51-050da89d2992 | -14.66711 | -46.56591 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5fb3014-b19a-3f85-a184-b2bcfc136919 | -7.93788 | -44.33164 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 421656a4-1e4d-398d-8144-62adb47ed89d | -11.82003 | -47.79299 | 2025-11-14 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e9bd71a-aeb1-3b3f-b422-035156b78721 | -7.84918 | -44.2967 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7ad50f30-b8cc-39ad-bd86-f467b76e4cbe | -12.0632 | -49.40883 | 2025-11-14 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 177b5c16-3bfe-3b11-8a45-8e1d04d81319 | -13.72794 | -49.13476 | 2025-11-14 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 496b1554-756d-3cbf-9d4e-d0d4b3cdb4fc | -7.93391 | -44.32621 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 435092b7-5e3a-310d-80ed-4c2162d3e204 | -7.93723 | -44.33641 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c4d8652-f9f0-3b9d-9eb8-3ad86eea4577 | -10.7306 | -44.02023 | 2025-11-14 04:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 96a78814-0ca0-3716-8da1-14444e6e43c7 | -7.93751 | -44.33863 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0cda407-246b-372d-9df0-f95832c73e61 | -7.93521 | -44.31662 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34186dfd-351e-3c48-a29a-5490c27c3fca | -12.67137 | -46.75406 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1da4be5d-3233-3de3-b53d-352876ed6bee | -7.86634 | -44.30895 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 002baf60-b5d7-3e58-b4f1-0d248f0dc2f2 | -12.70861 | -45.42944 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b8afba4-8ace-3ff1-a99c-eabe05ae9cee | -11.80254 | -44.26194 | 2025-11-14 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afc91438-cd1a-391c-a77f-161d2a60902a | -11.85157 | -49.2271 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 44d2f7ef-a6c3-3ece-8ba3-7dc3a4b68a07 | -9.67774 | -47.89242 | 2025-11-14 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aae68872-aa58-3894-a116-0457d08258ea | -13.84881 | -46.90454 | 2025-11-14 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c48933c7-5447-32a5-9cfe-1cac70b90332 | -11.94554 | -44.59861 | 2025-11-14 04:46:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0908a2ab-ce4e-3445-9d77-d25854e603a7 | -7.93853 | -44.32686 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dc9949f-15c6-3ce0-94dc-13201c9803ec | -10.3753 | -47.68747 | 2025-11-14 04:46:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f4fedd9-f9d0-392a-aae2-4939366d544d | -11.85219 | -49.22295 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c8efbcc6-b9d2-38b6-99c8-51625425857a | -12.41295 | -54.19321 | 2025-11-14 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a3a154b-bd91-3ccb-bdad-3cd72676f552 | -7.78845 | -49.62281 | 2025-11-14 04:46:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1655ced-59f1-3a10-a8e8-18b2307b76d7 | -9.04818 | -48.71579 | 2025-11-14 04:46:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce762491-7d87-309c-929a-216ed1b7bd80 | -12.62172 | -47.01775 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd95205d-c82f-36be-92a5-04d38b87d60e | -11.24536 | -47.50057 | 2025-11-14 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1df873dc-372c-3fa3-88b9-36130d354f8b | -12.689 | -45.43641 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 102baa1f-3642-3521-86fa-e22fc5a91a71 | -11.84563 | -49.2177 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c7939e3-b872-36e0-9c9a-cf0a314440b2 | -7.50857 | -43.0124 | 2025-11-14 04:46:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dee029ec-42db-395c-b426-7b58e2ec4690 | -11.73979 | -48.53938 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1ed9390-053f-3ac8-98e6-0fb387654e6f | -10.63244 | -44.82385 | 2025-11-14 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d13648b9-93ff-3266-a85f-13262ae13fd5 | -12.70989 | -45.41981 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe6a22bb-e266-36a4-8006-5c450add8fb4 | -6.83599 | -48.00478 | 2025-11-14 04:46:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d7e72ca-3e63-3a7c-96f5-f2c772f51c5f | -12.68184 | -44.1501 | 2025-11-14 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bce9939b-c254-3164-9c6b-523846886df2 | -7.83597 | -44.28993 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a68aa1ba-358b-3257-a5fb-25159a1202fc | -13.68624 | -43.0099 | 2025-11-14 04:46:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6f02528b-fdd8-359e-a7dd-4484cf53821b | -12.6247 | -48.40501 | 2025-11-14 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 931cd9b3-8b6a-335a-9ab1-a2c7a1b18047 | -13.96716 | -47.04922 | 2025-11-14 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31c3cc00-7796-3877-97ab-1931406a4b9a | -11.31168 | -48.50647 | 2025-11-14 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7661cca5-e1cc-34aa-b3cd-5a6fcbd6740b | -11.82073 | -47.7881 | 2025-11-14 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a03d7c2b-9e06-37c8-ab42-384533d36bfe | -11.93366 | -43.94621 | 2025-11-14 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ad22fa1-b093-32f6-ba6f-563eb5268b03 | -12.29617 | -47.90874 | 2025-11-14 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2e7e8d6-c8f1-36dd-95da-6407d33accb7 | -8.91021 | -41.07878 | 2025-11-14 04:46:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 960fb3b9-c27e-38df-8619-5b775ee56a0f | -9.34529 | -46.59116 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 90674d9c-0401-3f5e-865b-d380e3c50796 | -7.84125 | -44.28577 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed63dc14-7c40-3c3f-8f7b-6655391d635b | -14.66657 | -46.57004 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6a5ad62-f33b-3a58-8f55-701aa3ca2f8c | -7.53985 | -45.85832 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 189d48ec-fb0b-3ed2-bc89-34b39642ac02 | -12.07923 | -47.88774 | 2025-11-14 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1a2b172-f238-306f-9e5a-436c733e5cd3 | -12.01573 | -46.76798 | 2025-11-14 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38773598-4d7b-387f-b847-989494a831db | -14.67602 | -46.56579 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfe9d126-6dd4-33b8-91d7-85ed8bbe1e98 | -11.74044 | -48.53489 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a40a762f-e539-383c-aad6-d2e4e70910d2 | -12.66718 | -46.75345 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 03385325-9c7f-3232-a6a9-33ffa4bde701 | -11.3191 | -48.50742 | 2025-11-14 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c095784-7cf8-3fac-a1db-628c74f63145 | -12.09342 | -46.4762 | 2025-11-14 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25985276-dd5d-3b70-9d1c-2ff7f21b8d13 | -14.67155 | -46.56596 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f713ab8-a953-3b81-b38f-12a6aef5d8c9 | -10.75526 | -45.02115 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README47.md)
