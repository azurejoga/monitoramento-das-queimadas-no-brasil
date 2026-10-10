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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6350c4fe-e001-3d88-b28a-ed6f713383aa | -12.77708 | -44.88948 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 517b9163-d55d-3d1f-8d70-7fd0927d73e7 | -13.17572 | -48.12788 | 2026-10-10 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a42f916d-46f5-36af-ae0a-a7e252e0432d | -11.01774 | -45.41891 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9cfa246e-589c-304b-adda-0ae604623c11 | -11.58728 | -43.69423 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6f8102c-9a1c-3b41-af37-de87d67fe1d0 | -11.65583 | -43.66972 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02f34849-72fa-3605-a486-18a3e7f4a81e | -12.86471 | -39.9236 | 2026-10-10 04:10:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fbcf7c57-88d8-3e06-885f-357dbfcd101c | -9.0969 | -54.70653 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47408063-1d71-33ea-85e2-f13818c088d6 | -11.12628 | -43.2513 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 03a23e2b-d58f-323d-b4a9-392e6c6404ab | -17.97482 | -44.34258 | 2026-10-10 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efaebc87-1f10-39d9-9829-0f0beb9706b7 | -13.51512 | -48.61209 | 2026-10-10 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7328334b-a762-3ddb-8e00-9ee88d42342e | -8.65256 | -54.53482 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d33ed521-722c-3222-8e48-ff1f69b2a170 | -13.10745 | -46.35735 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b19094f-87f2-3afa-858a-def702edab19 | -17.72228 | -42.04704 | 2026-10-10 04:10:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fd5382a0-2484-3368-bee4-155765936f50 | -12.2287 | -44.68837 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68338433-240d-30c3-a4d1-18d5d4dec741 | -11.69563 | -43.65454 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9313a44e-48c7-38ca-8fd6-1134cce5535a | -12.12372 | -43.31668 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e974563-073a-32ff-bce8-34022619aaab | -11.97067 | -43.48591 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e0d7661-cf61-30ef-87ee-f57af5059e40 | -14.24338 | -47.30605 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1530dd1f-be10-3168-89df-b0e2c1010181 | -13.63298 | -44.42133 | 2026-10-10 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1330fd8e-6a67-37fb-a430-46198fb61c15 | -8.64611 | -54.53367 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4227481d-73fb-3f7d-8bad-12fe8b694467 | -14.45575 | -43.93587 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3169fc03-3f54-3ff9-9547-1f6a32618520 | -13.26171 | -43.99642 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b247b382-650b-3a7c-8efc-f46b0168a70c | -11.12958 | -43.25184 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 02e489af-f5a5-3190-984a-9b3c1a83ff02 | -12.36631 | -46.60667 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3c785a4-21b4-385c-aece-babd789fa74b | -16.5924 | -46.77514 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d955083-9937-3300-96b2-ec35c206fcfc | -11.96187 | -43.47727 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50d7c6c5-06fd-3698-99a7-81a810772595 | -11.94096 | -43.48096 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33b83e74-bd95-3e93-b27d-27ec77e3703e | -18.09064 | -42.25692 | 2026-10-10 04:10:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0b18aef2-f0db-36bb-acd3-d9d3b800a3d1 | -14.71873 | -48.21834 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0224d0ae-ece5-34c8-8dd0-99eeb1d9dfee | -16.14054 | -46.03413 | 2026-10-10 04:10:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7d0ebac-2fb4-3e01-a133-bc4bf266ca90 | -14.33387 | -55.01897 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbbbdb19-4a61-390d-950f-1bcf44925ecc | -12.29805 | -47.04774 | 2026-10-10 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7156f8f-bfbc-3336-80ec-fec07dfa5cbe | -13.50895 | -48.59976 | 2026-10-10 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b5a85e3-de7e-3363-bc03-76caf0cf7476 | -13.52133 | -48.43475 | 2026-10-10 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9509f1b1-38d3-3a25-994a-6be5cd12c6fc | -14.02184 | -48.75837 | 2026-10-10 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf56f628-544f-3690-b5f0-58dde22136af | -11.99818 | -43.4439 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4c45d49-bf51-3ba1-93f0-d272ae91d8f5 | -10.88419 | -44.78951 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5f3cf2c1-bd0e-3260-89b2-17cdc1f487ed | -13.38258 | -43.87798 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2fccf37-2037-3f7b-adf3-af8b7e02c60a | -15.11732 | -39.92292 | 2026-10-10 04:10:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f73592b5-394c-3c62-9608-a5b2ec9671ca | -11.02626 | -44.04932 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f114716c-babf-32c3-9a1b-f73ec664a3a6 | -11.97344 | -43.46833 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfd438b8-3651-3b90-bbb0-a86b5e58317f | -10.86144 | -49.14084 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a43722f-4a49-3569-9ed9-c667faa1d107 | -17.28764 | -41.22065 | 2026-10-10 04:10:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9d3a26ed-87ad-34b4-af74-bbfc59af7b7c | -13.5117 | -48.60782 | 2026-10-10 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6821de01-8d08-3e95-9b94-44152b8a61e8 | -14.55928 | -48.0209 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 23184751-818d-3ff4-8480-162b0c8a2c8c | -13.73818 | -48.51173 | 2026-10-10 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 878cf11f-3947-35f8-b519-bbb6656101f5 | -11.97841 | -43.45829 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d09852d0-dedc-3abe-a997-71f9ff33546c | -11.38932 | -47.58385 | 2026-10-10 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7bfee28-e806-3158-9b6b-ea9b75b6e30c | -14.4623 | -43.9588 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92e22ba5-9794-3517-8762-818208e0acc9 | -11.46719 | -43.37878 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad55ce7a-35e9-377d-961e-bcfdfda339cb | -10.49607 | -47.33571 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b2364ae-0d4a-3758-abc3-1497e71ce39a | -12.22171 | -44.64561 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df2e06c9-d75f-340a-bf07-1aef58fc18ed | -15.63742 | -39.18268 | 2026-10-10 04:10:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f2d2b408-6206-3536-a9d1-0e4b532b5206 | -11.92584 | -46.76482 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba8a55ba-01f5-37ec-b2df-37488f36cb72 | -9.96305 | -55.33067 | 2026-10-10 04:10:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb8ed1a3-467c-388c-8c29-41e9288be0e6 | -15.02122 | -46.26423 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04dfde1c-1a76-34b2-86c4-048f0052e89b | -11.08452 | -44.11437 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aca2b060-e548-3bc9-b8d4-a98fe0b39dda | -14.05608 | -43.83699 | 2026-10-10 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25da5920-b15f-301b-b5cb-bdf5a81a8e0c | -11.68161 | -43.48598 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7577a9b-195e-3265-b9e2-8bd190dfb406 | -12.86831 | -39.92425 | 2026-10-10 04:10:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 02f82299-4730-3588-b46f-7041f847441a | -14.44971 | -43.93123 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 786b2d4e-0016-3df0-b04c-eaa466320369 | -15.38762 | -41.89767 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4af2f047-538a-3ec1-8fd0-75b9c75b2e7c | -15.26148 | -47.92581 | 2026-10-10 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a55f65c1-90bc-313a-812d-5f0e6a7dc4d7 | -13.74625 | -40.83638 | 2026-10-10 04:10:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d898ef10-389e-3ede-8beb-95121f410c43 | -15.37454 | -41.93507 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| bfadc004-a2a6-341e-acba-0eb3c98d6292 | -11.57119 | -43.70983 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aae68993-749e-3e79-b184-c20736a1ef5e | -11.3828 | -46.66332 | 2026-10-10 04:10:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8d1875bf-5b75-3971-b865-f4ec50af212d | -11.20765 | -44.85422 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47662be2-b313-32d7-b329-92f2c6132844 | -16.8583 | -40.36459 | 2026-10-10 04:10:00 | NOAA-21 | PALMÓPOLIS | MINAS GERAIS | Brasil | 3146750 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6023a744-c865-3760-b3be-f65991283986 | -11.86952 | -48.02954 | 2026-10-10 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e92b47df-6190-3b71-ab4a-1591489fa1a7 | -8.50467 | -54.60886 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0c1e7a3-8457-30de-b5b6-9ef74721082e | -11.59291 | -43.6373 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16fc82b7-e86c-3f16-9f4a-466aa9566c94 | -11.20117 | -44.87254 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0918eb51-1099-3a66-928e-ccb8b7d0035f | -13.77679 | -48.12905 | 2026-10-10 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34bd5ee7-b42c-3525-b72f-fa4353897f06 | -17.14225 | -41.35478 | 2026-10-10 04:10:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 72922185-dbc4-3c98-8766-0fe1827c499d | -11.08349 | -44.09938 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a8311ef-86ae-3a12-9c02-fdc0d334ef25 | -14.44691 | -43.94897 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 534d5bd6-7729-3403-8e2a-86cc4aaf5db2 | -11.2472 | -44.84853 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0050732b-9297-393e-a765-421e3ac2d389 | -16.56652 | -46.79971 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0c8f18f-436f-3fae-a9d7-23cb3c1ab5e1 | -15.24891 | -41.88501 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b3e3cb15-922a-3539-ba10-8210d890f25d | -14.46068 | -43.94761 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 802342bb-f786-32cc-95e6-af278fb39a3d | -15.07953 | -48.46178 | 2026-10-10 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d367e9a-4445-3bad-81df-6c142a359da4 | -13.53471 | -47.41859 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7fa757a9-c9f9-35a2-a661-3e7d94a11d61 | -12.24303 | -44.75875 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e89b803d-cd2d-38f2-98a6-4574df5619e6 | -15.24396 | -48.58115 | 2026-10-10 04:10:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 813ca99c-81ef-3ffc-a45f-9e279bae60e9 | -15.42599 | -43.32029 | 2026-10-10 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| add311a0-d76c-3266-b556-cc2444929148 | -10.73162 | -52.03395 | 2026-10-10 04:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea11cc2b-8ad4-39d9-b38c-7819e773c709 | -11.03205 | -45.42575 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bc7b52c-297c-3a5a-b5be-982b63431697 | -17.44819 | -45.06857 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 386f837a-f8fb-37e9-9a38-c9915bef0448 | -10.89605 | -44.8031 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1146c14e-885d-3ada-8674-7baac1d53eb2 | -11.59611 | -43.70291 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05690960-a62d-3adc-a1be-15ab93b91f8e | -11.67748 | -47.30037 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cde6d21c-0f1f-3459-b62b-47bea1e0b708 | -11.77835 | -45.50543 | 2026-10-10 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 742af72e-4e11-350d-9b8c-ee310ec90f83 | -14.45626 | -43.95415 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1ee8e798-9366-30b0-b7c5-c42870f2f5fc | -15.05844 | -41.7983 | 2026-10-10 04:10:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 33ea4e87-87fb-36b6-8052-2876fbc3e071 | -11.86173 | -43.55108 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ee957d7-3f20-345f-8ee5-0561ed0bee01 | -11.59931 | -43.74711 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 48cd6b65-36ed-34e1-af5a-730334199692 | -15.40069 | -41.90353 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| ae1b76ec-0fef-3cab-a97d-2e78ce08c3ad | -13.13163 | -46.3226 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd679c43-e7d5-3da7-9dc0-680fd46459d2 | -14.38799 | -54.96826 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README52.md)
