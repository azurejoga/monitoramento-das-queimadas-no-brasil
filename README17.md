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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66d4d0bc-28b3-398c-b14b-d0518f34701c | -3.11014 | -45.76987 | 2025-11-13 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07b384de-d158-335e-8d74-933da0225597 | -5.36739 | -45.07858 | 2025-11-13 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc444b08-dbee-3f8f-b798-0467146a0394 | -4.57411 | -46.93945 | 2025-11-13 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a8b0c8d-57d4-3397-bcab-1f633a099880 | -2.94626 | -45.54939 | 2025-11-13 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ca16221-eee6-3b11-998f-50ab9b7ea279 | -5.83795 | -47.56135 | 2025-11-13 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e1acae6-690a-3da0-ab9a-8280d66b8d0d | -7.22467 | -47.98621 | 2025-11-13 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b52bb092-53b4-395c-aaab-bca7e4a7b0e9 | -9.32797 | -47.83937 | 2025-11-13 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 386d6f35-b651-311a-8b36-c9afa2bb5c81 | -5.35576 | -46.75922 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b0161b4-a819-3c69-bfea-91128288d2b1 | -6.74043 | -42.5303 | 2025-11-13 04:14:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 73c77b4a-d33d-31b3-8601-704ba899a9e8 | -10.20472 | -36.23426 | 2025-11-13 04:14:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| e8c8ec4d-0bff-34d2-8fa6-0034cb6252c3 | -7.37624 | -41.89115 | 2025-11-13 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0733feb3-138d-3454-a7f8-bc64da2ca0c4 | -12.11007 | -43.64517 | 2025-11-13 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7891384-38eb-328b-b4d5-238a3d57cdcb | -10.44622 | -47.33828 | 2025-11-13 04:14:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0acb8b22-0f90-3e1a-ba15-2e5b6b9bd05f | -7.16859 | -39.36324 | 2025-11-13 04:14:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3f09783e-f52b-3701-855a-b67c1f297933 | -7.45562 | -42.56788 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4987f36b-1d6f-3c84-8ce2-69a1a1480a02 | -6.57382 | -44.04317 | 2025-11-13 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95cd977b-8f90-3aa6-9001-9d2b3866296d | -7.48538 | -42.55104 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 886b325f-63f9-3c69-934f-e80fb7e85a85 | -12.64786 | -46.74191 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 32d01304-ab55-35e9-bb7a-1e729e90cc9a | -11.73644 | -43.84156 | 2025-11-13 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5672b30d-9c81-343e-a8b5-12ee32fb55f0 | -6.99468 | -38.05099 | 2025-11-13 04:14:00 | NOAA-21 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 64c1ece0-5b85-31e0-8d70-fe340c8ada60 | -9.66637 | -43.89845 | 2025-11-13 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4aaa7218-f5df-376c-848f-1afe8cced95b | -13.02672 | -46.53117 | 2025-11-13 04:14:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8f306de-c77d-3ae0-8ac0-9e5f4b13c910 | -7.18466 | -44.98586 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 653ca39b-9069-3b44-9963-2fa580cbfc2b | -5.39337 | -48.33167 | 2025-11-13 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a53495f-b116-3614-81ca-0b74e0055ffe | -10.35422 | -47.70385 | 2025-11-13 04:14:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a5c69c8-62ea-3f2a-b1b0-9aac2bbbaf71 | -10.63294 | -45.24287 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca56fe25-6b65-3c85-9e79-b67ae521f9f4 | -6.29241 | -41.73193 | 2025-11-13 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 00cc1907-91c2-3354-8af9-236d8e33fbfb | -7.24721 | -41.62887 | 2025-11-13 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 51b8de1a-f147-3d63-822f-6cc10d781279 | -7.40177 | -43.326 | 2025-11-13 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf8ca744-b934-3760-bd16-cb45b3fd0b62 | -7.22622 | -47.98425 | 2025-11-13 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb094c1c-3857-3cc6-b2b6-1148ea6a0830 | -12.03715 | -43.87564 | 2025-11-13 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c0fc0e9-023c-31bb-87e5-37d00287afd3 | -7.01574 | -42.15831 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 234fa8a7-d68a-3382-b7ee-a0c26e4ca1ce | -5.66435 | -46.284 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91b0a060-e196-3acf-8508-8ed877282576 | -7.7151 | -42.3398 | 2025-11-13 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ba4412e7-8811-3ec6-a534-5851f886105b | -9.42471 | -37.32904 | 2025-11-13 04:14:00 | NOAA-21 | CARNEIROS | ALAGOAS | Brasil | 2701803 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a28287e-ae84-3f22-8d1d-43965eaf887b | -12.98833 | -43.59208 | 2025-11-13 04:14:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36a474a7-b0ef-3607-b3a1-7c5c44893b2d | -10.82631 | -44.65351 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aef285fb-8229-32c8-8329-ae4e8e9f04c3 | -7.22265 | -39.95357 | 2025-11-13 04:14:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5e077ce5-9cca-3e27-959c-110495de0192 | -6.29731 | -47.01262 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a89b0a6-2bff-3dfa-b79d-0a02f0fbfaaa | -9.00015 | -44.17349 | 2025-11-13 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df2b77c4-1fb2-3d38-9d74-21881aaccbf2 | -10.16033 | -46.56727 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 063f1e9a-29fd-39ee-a707-f5ae2f513480 | -9.198 | -49.47921 | 2025-11-13 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab5187b0-7c9b-30e7-9caf-c46573b45ac6 | -6.15843 | -48.05212 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7ebe09c4-53d3-31c2-a86a-c651cd44e720 | -10.92525 | -44.62991 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76ec71fd-5baf-34aa-87d8-7bd7ff00493e | -10.92194 | -44.62938 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9ca961d-1f72-3762-9e54-6003edd9f319 | -13.17521 | -43.05394 | 2025-11-13 04:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29d30817-7c99-3cfc-9ce6-2bb2ae84052f | -7.06662 | -38.65095 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8408f156-e68f-3bab-9d89-f49a8529309b | -6.42171 | -42.17348 | 2025-11-13 04:14:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 61cc38e1-8100-3cca-93a0-34a7981aaeaa | -12.66656 | -46.74906 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| bea8bd99-d4eb-3c00-a81e-26409422443b | -7.71825 | -47.18837 | 2025-11-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 571b72c8-a7b1-3b0c-b36b-b7b38c217c26 | -10.7103 | -45.08238 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ca423d0-dcc0-3f12-b0cd-7589f1f2c3c0 | -7.21913 | -47.97789 | 2025-11-13 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ba311d9-48f8-312b-a2d0-76a888858b35 | -7.81351 | -41.78548 | 2025-11-13 04:14:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6f573f6b-9a96-3bc2-8bda-0e676ae5adc8 | -5.66053 | -46.28497 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a31dab2-3fc7-34d8-a75f-cd303558a37b | -6.90021 | -42.06857 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bf19578d-6927-369a-a2bd-149588334bac | -10.20461 | -36.23227 | 2025-11-13 04:14:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 8bd53f7f-8741-32cd-8e3d-16cf0f63d4de | -9.44323 | -44.87595 | 2025-11-13 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dfa6319-f42a-3eb3-9419-ee18beafb648 | -12.65133 | -46.7425 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 476f0ebf-8d82-3444-b16e-8d054d7a279c | -12.65415 | -46.74698 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ee104f2-2b41-3a50-b080-f7a705afef99 | -6.5482 | -41.7062 | 2025-11-13 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5a3325b-be88-379e-bd73-91054f499105 | -10.61899 | -44.82242 | 2025-11-13 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64eb2d87-7e4d-335d-b1fb-d34f3ec7ecf9 | -7.38435 | -42.58891 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4f47a7c-aec6-3ed9-a0fa-967cfc23a543 | -7.24665 | -41.63247 | 2025-11-13 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 84820343-62bb-39f4-91bf-5aecb771bb12 | -10.63235 | -45.24648 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25b819ad-381b-33e3-8df1-9ab7bba21c09 | -5.35953 | -46.75986 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbdafa85-3504-30b9-b93a-a1c12a23d31d | -12.66244 | -46.75237 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| ab50f0c9-02c1-39dd-a039-e6c6a07cfdbb | -10.66683 | -44.47929 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5ac4607b-1805-35da-8f14-1345158b171c | -10.62565 | -45.24538 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96a51cd0-e04e-347a-9d6a-7490fed76710 | -5.72656 | -44.83209 | 2025-11-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a10278f-e291-3402-a7df-bdbb3e324d78 | -6.90355 | -42.06908 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b166d96d-4b3f-3607-8f65-65b7b1478288 | -6.90138 | -42.08318 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a401ee9a-2f6b-309c-ac98-9f699a475bd0 | -8.5544 | -48.01562 | 2025-11-13 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce1a1bf0-5485-33f7-acaf-0452ee4fbf7d | -5.73074 | -46.55051 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1c12758-7761-3a99-84fd-cfe828981ca4 | -6.14563 | -48.05404 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10fdc701-d64e-391d-aa76-f7d484cee353 | -9.64453 | -44.55183 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78f71c67-c64c-3a48-ad56-a061a1c34b70 | -7.15252 | -41.70665 | 2025-11-13 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| da250998-77d4-3a8a-9814-a565d54fb4a7 | -9.05875 | -48.83205 | 2025-11-13 04:14:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6996ed2a-46e4-39a7-be8a-f5bce8fcec91 | -9.06282 | -48.83274 | 2025-11-13 04:14:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c03f976-626d-3eda-84ba-d2dcbcc95c87 | -11.0609 | -45.37603 | 2025-11-13 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e358ea6-4006-3a1a-b83b-475c3bb49e64 | -10.60455 | -44.82734 | 2025-11-13 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ceddf1d5-b199-3dc9-b4fd-19825257f660 | -8.85033 | -35.17191 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aa61400e-a73e-3c56-a530-b7dd4f7fff4d | -12.0424 | -43.51114 | 2025-11-13 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 522a8ac4-6bfd-3cb0-b083-4c8aa2f737a0 | -5.38569 | -46.76738 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1817dec-7992-33a8-b14c-8438fb5b52b0 | -10.88688 | -44.40048 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57ff9517-225f-3998-b2cd-f59a74316cbe | -6.31366 | -44.30715 | 2025-11-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0cc7819-16fd-3593-8116-6dfab1848688 | -10.4962 | -47.98896 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de69b04b-e9be-3a27-a50d-9cf689a936cd | -8.25455 | -44.37017 | 2025-11-13 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f621d47-f68b-33aa-95a9-2d9da9638c02 | -8.86518 | -50.19226 | 2025-11-13 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6610d766-5b6a-36ce-8bb8-c34378c4bea9 | -9.92655 | -48.14302 | 2025-11-13 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0da84fb6-9b90-3522-8f39-efc2333ae09a | -9.67022 | -43.8955 | 2025-11-13 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6bda1b22-eb3b-36af-b2e5-6f7546c6fc0f | -7.15306 | -41.70306 | 2025-11-13 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c80773eb-1f45-3907-bd6f-01a64ceb8195 | -10.78093 | -48.14524 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f53ed1e-89b2-3a28-8d88-0cccb281eb26 | -12.50481 | -46.30491 | 2025-11-13 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5083f04-4eb8-3683-ae27-1368ec5cbdcf | -6.14094 | -48.05711 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9eb02833-c86b-3a79-91b8-609c4cd63c9b | -6.24583 | -42.36367 | 2025-11-13 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 205a3d12-a233-325a-a9c3-270ba9907b66 | -6.25594 | -44.83855 | 2025-11-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 883cc97e-14b1-3078-9707-c792e652e419 | -6.47557 | -43.95528 | 2025-11-13 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e693c00-0bf5-3d9f-970f-f1e9f15c2449 | -13.02662 | -46.5312 | 2025-11-13 04:14:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b141d8d9-fa92-3c38-ac23-453e897da02b | -13.33082 | -43.17618 | 2025-11-13 04:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e40f902c-0e71-3538-b9cb-d9c4e81bc445 | -10.19501 | -44.89917 | 2025-11-13 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README18.md)
