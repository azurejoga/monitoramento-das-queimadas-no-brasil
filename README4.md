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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ba8b982-0bbb-31e7-9fc8-1548e1d1dcc7 | -3.96178 | -46.99153 | 2026-01-11 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c741c88c-b8f8-390c-88ac-11c8b96ce705 | -2.52109 | -43.26162 | 2026-01-11 04:08:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 18746f08-aa59-324f-99b4-82ab9d4ba838 | -3.64293 | -42.02662 | 2026-01-11 04:08:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc6b20fa-c4b2-3bc0-acc5-3cf57a914299 | -5.46384 | -45.28524 | 2026-01-11 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3fb4e98b-c1dc-3755-bc34-6151f25f140e | -1.49709 | -45.91496 | 2026-01-11 04:08:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afc16a76-5cf9-3a5c-a736-b8eb34c75139 | -5.52808 | -42.84685 | 2026-01-11 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 832718e5-31cd-3c96-b311-b80fa7088ad4 | -5.85499 | -44.95037 | 2026-01-11 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f8065e9-2a34-3397-9bd6-72ab731b8adc | -6.22817 | -44.15879 | 2026-01-11 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16157e77-4d2e-3753-bc60-f99ee30415c1 | -7.59582 | -45.88968 | 2026-01-11 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5228ed5-9bff-3d38-af1d-7fb63a771c2d | -2.19053 | -52.01645 | 2026-01-11 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 530044b7-961b-36a1-8d1e-7c4014e4151f | -2.86922 | -45.23867 | 2026-01-11 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1419283c-021f-36e3-8f04-648a93882aab | -2.19146 | -52.00965 | 2026-01-11 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ddc003b2-68b6-3087-8f95-eecfb109792c | -7.38068 | -42.79338 | 2026-01-11 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f73f0181-593d-3b54-a6f6-8a5d618fdfa1 | -3.49537 | -41.71078 | 2026-01-11 04:08:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e5b306e-84fb-3ebe-82e9-b21b49e3b679 | -2.18532 | -52.00867 | 2026-01-11 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9adb060-e2a4-328f-a363-fd342848adb2 | -5.24049 | -40.82404 | 2026-01-11 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 966d1494-f718-32b1-8df5-5a4ec0e3163b | -2.89089 | -45.22722 | 2026-01-11 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39e3d0aa-3a31-303b-a240-23d42d5b4222 | -1.43002 | -46.01526 | 2026-01-11 04:08:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3afa069d-c5b0-37f0-bd5d-6bcea1bfb793 | -7.45249 | -34.86177 | 2026-01-11 04:08:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3c29aa2f-b5da-3760-97d9-60cb163159c5 | -4.2999 | -48.06921 | 2026-01-11 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5621d03-4f1c-3036-9e2c-ea982a5efd74 | -5.58564 | -40.8998 | 2026-01-11 04:08:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4d3f4d78-a2f2-3297-9037-023adef24c5b | -2.62304 | -43.10058 | 2026-01-11 04:08:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b517fa8-19f3-39bc-a1e6-a152ada42692 | -5.13133 | -46.12541 | 2026-01-11 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3211766a-d938-34a7-8ec7-af2cce6ffda1 | -5.8557 | -44.9461 | 2026-01-11 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e66f4bef-9bb4-3ae8-8fd8-790c1100bfae | -2.8693 | -45.214 | 2026-01-11 04:08:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 067ff0a9-202a-3c03-9ef7-feec11640fac | -5.181 | -44.75539 | 2026-01-11 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f0d29d2-6c06-3231-b632-3b0b44b61b2c | -2.87623 | -45.22002 | 2026-01-11 04:08:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e518377-369e-3d3e-9e76-f859c2a87d13 | -9.97249 | -36.36402 | 2026-01-11 04:08:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a0d5b48d-1009-343c-9ff1-154cbbe90fd8 | -1.02554 | -47.6894 | 2026-01-11 04:08:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98ee6279-09d5-369e-8f43-28f5769f0724 | -6.22881 | -44.1549 | 2026-01-11 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a03eb33-5c55-3724-ab34-b8764bacc9f3 | -8.2363 | -35.35254 | 2026-01-11 04:08:00 | NOAA-21 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 412ff942-c726-3c0b-9d4b-da6bdaf6437e | -1.0842 | -46.77471 | 2026-01-11 04:08:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 668fa68b-4e70-3f82-b377-1135d02ca132 | -6.02017 | -44.54875 | 2026-01-11 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e284c79-4902-3887-aaa4-62df47eaa781 | -4.81627 | -45.23612 | 2026-01-11 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6d908a2-1a2a-35df-ad47-004ec845ddb4 | -5.4601 | -45.28461 | 2026-01-11 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 857a46fe-bcf6-3219-9e83-7e905e7b73ed | -5.18973 | -37.57219 | 2026-01-11 04:08:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 196f4ec2-db2f-3298-9f1c-186c7023753d | -5.34292 | -38.29175 | 2026-01-11 04:08:00 | NOAA-21 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 015d42a5-7f6e-3451-9605-48fb764e47f4 | -3.49869 | -41.71129 | 2026-01-11 04:08:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c47a4cc2-d774-35d7-b562-16244898dc57 | -5.50084 | -42.15636 | 2026-01-11 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4a66df83-468a-353d-958e-4428adcb1d3b | -2.18452 | -52.01337 | 2026-01-11 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee202c8a-1700-36d9-b627-78763614bc2d | -12.91521 | -52.52845 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0e7fdbe-a90f-38ab-9be9-06300391cb9f | -13.76664 | -46.63422 | 2026-01-11 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d591f2c-d051-3dff-99bb-a579499665d3 | -12.54053 | -38.26643 | 2026-01-11 04:10:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 50204475-81f6-37a5-abff-6c1f926576b0 | -11.83718 | -49.19664 | 2026-01-11 04:10:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bd0d25a5-8d5b-3354-a49e-e63cdc4d86cb | -11.03243 | -37.11953 | 2026-01-11 04:10:00 | NOAA-21 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4ee81368-2bc7-35b8-be13-b05cad42bcaa | -12.78903 | -42.38258 | 2026-01-11 04:10:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d90978c-0077-382e-923f-9f3adfa7ff9e | -10.29318 | -37.05936 | 2026-01-11 04:10:00 | NOAA-21 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d5cfad67-cdaf-3617-8659-d858e0ce178f | -10.84765 | -44.03527 | 2026-01-11 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e941ebbe-6d8d-3de7-b38a-2f75c27709c1 | -16.31217 | -45.10606 | 2026-01-11 04:10:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fcc7a04-87b3-3214-aac7-1699051a3373 | -9.04728 | -46.99322 | 2026-01-11 04:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 556ba174-18dd-39bd-a3a0-695103117fd7 | -13.40781 | -43.75423 | 2026-01-11 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 116b6311-9145-3859-97fb-f13add2da210 | -10.77202 | -45.01625 | 2026-01-11 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e3aaca98-32ac-3549-b30a-dbdc0e43be13 | -12.90396 | -52.52966 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e87ad0d5-30aa-3e37-87f6-6fccdcdbe7c3 | -12.90464 | -52.52625 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 525d9e4e-d4c8-31a1-9307-dc0eef782ec3 | -12.89934 | -52.52517 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18e9f9ea-298d-3b91-9273-f68964653391 | -12.91059 | -52.52393 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d9308f9-aecb-3142-bbfc-8d2d722d17b5 | -13.81648 | -44.41272 | 2026-01-11 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e552f97-4db5-360a-ad32-d1563ea5a953 | -12.89867 | -52.5286 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf9a43c7-ffd4-3284-93e5-2415951be7a5 | -12.90001 | -52.52177 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67fd4474-cb03-3216-8bd8-6d4a899a23ab | -11.16851 | -43.30564 | 2026-01-11 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 480db999-1637-3b55-97d9-f11e271a339b | -12.50705 | -46.68042 | 2026-01-11 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fc5edad-7069-331d-b4f8-77e69cffc4c8 | -12.9053 | -52.52284 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d15c2561-c3ab-3572-a69e-906f001a7a60 | -13.43247 | -43.85693 | 2026-01-11 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8acc3338-011f-30aa-ad22-3e8e284f0d52 | -13.34277 | -41.33076 | 2026-01-11 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3678f027-e134-3642-b75a-a7f61719c75c | -9.05122 | -46.99385 | 2026-01-11 04:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 651e9bac-f9bc-37cc-b5ed-64bdb9881612 | -12.60577 | -43.31799 | 2026-01-11 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cc5ba4ad-430f-3eb0-8a4e-58f2b928960e | -13.12261 | -46.7061 | 2026-01-11 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71e540f1-d1dd-302a-8ac0-aa220cda6f58 | -12.90992 | -52.52734 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56d607d3-8acc-3c32-a6b6-c08d99520bfd | -10.25125 | -44.89248 | 2026-01-11 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d195d63-06ab-396f-bca9-3f9b6c96ecde | -12.90925 | -52.53077 | 2026-01-11 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9e82d00-299a-310a-960d-b856034a41e2 | -15.25852 | -42.87798 | 2026-01-11 04:10:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d030823b-9302-35c4-a4c5-26d1328fa08f | -16.30883 | -45.10548 | 2026-01-11 04:10:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 433933e5-ef06-3b80-9a44-c5f3317d23e0 | -16.05155 | -47.21434 | 2026-01-11 04:10:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31fbe829-605c-3d05-bcbe-bad59b1747d1 | -11.02773 | -37.12277 | 2026-01-11 04:10:00 | NOAA-21 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3939adf5-625b-30a9-b9dc-7e415aa722b6 | -11.83793 | -49.19244 | 2026-01-11 04:10:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| facff914-a89e-3965-8e7b-21b74bb0ad00 | -11.07524 | -48.26577 | 2026-01-11 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a6ddd54-d91d-3151-a6e3-6e600957efab | -19.0665 | -44.32687 | 2026-01-11 04:12:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63e38a68-e73c-3495-94b7-a79bc9d45191 | -18.82586 | -51.62032 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 248f928a-0830-3e46-806c-6fdd9519ce92 | -18.81622 | -51.61106 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| dad3ed12-62e5-32a2-850f-a91b1ea7d87e | -20.25774 | -46.51318 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31646685-e134-3ae0-b663-b181608b3440 | -20.25711 | -46.51698 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c183603-a0f6-3591-bb27-0eaac147146c | -18.81891 | -51.62127 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e688eff9-3080-30d4-a95d-106b0a457cac | -18.81878 | -51.60915 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c30f1730-a5e4-3799-a327-09dfbd52f995 | -20.23589 | -46.47748 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d0cddc3d-964c-38f7-b0b5-6b7cec429b8f | -20.13909 | -46.84582 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0c8c3c9-c252-3962-876c-b281cd71938d | -20.13975 | -46.84193 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d4223c3-f14a-3808-80f8-35c1ddf45e66 | -20.13225 | -46.84467 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fbe70c4-f302-30a2-bcc3-0e10cbc382b7 | -16.09942 | -56.75547 | 2026-01-11 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 513d8261-23e3-38bb-9c15-2e272cd07a32 | -18.82517 | -51.61289 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2f89cfdb-d00c-35df-90ce-f2949da7e65f | -19.94825 | -44.71341 | 2026-01-11 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff32f723-a8b7-3c55-8abe-0918069f44bf | -20.25227 | -46.50425 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2168ddf-4d7d-30ee-aa9d-14c5e8d4eab7 | -20.13159 | -46.84858 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c7d00d0-d087-33b9-bc5a-0661b674d506 | -20.13117 | -46.84937 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95b76407-5949-37ab-85f3-6174425486c9 | -20.24294 | -46.39321 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4203f84c-95f6-384d-8afa-a76483fd0b14 | -18.70661 | -40.00565 | 2026-01-11 04:12:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cee1f5c4-6e6b-3f8b-8976-6941c5056fd4 | -20.13182 | -46.84547 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 444aa88d-82c4-3798-a214-db3b94462053 | -20.13567 | -46.84524 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54ff4df5-d10b-392a-9a8a-76564ece3a34 | -18.82161 | -51.60723 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e41cc83b-22fe-37f7-b03d-6b42c7aa826a | -20.24681 | -46.49535 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 418bcd15-78b6-31f9-8564-3dfb96145a43 | -18.81173 | -51.6102 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README5.md)
