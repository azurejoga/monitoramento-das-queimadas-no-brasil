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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 033470e5-8958-39e2-b45b-302450f2eefe | -10.56518 | -49.83245 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a08d275e-0f05-311f-b658-6bf05a69531c | -12.52986 | -47.54638 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bce26d81-fef8-3b45-8dce-b660a02b88f5 | -13.63348 | -47.61872 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a30a767-cba2-3214-ab12-8ac105adacd2 | -9.57358 | -47.89836 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9221a587-c527-3aab-b4d3-48c58f56b985 | -10.94888 | -50.26895 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 074cac6a-cda7-38f7-9dd4-7483fccccc59 | -11.16389 | -47.78135 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 369c6b8c-7400-3e10-8b1c-f19d801b4872 | -13.08576 | -46.68505 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d7df60a-e1f6-3624-80b8-b09f171a7e17 | -10.32228 | -48.78885 | 2025-10-28 04:44:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 075cf505-8ed9-35f0-8d8c-5ddf31f22d93 | -10.28972 | -47.22964 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f658778c-3df6-3b36-b3e6-84aed9b4b5c9 | -13.2494 | -47.96666 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e251ecca-4c16-3798-8a62-d4a2155c997b | -10.97105 | -50.25808 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd12d101-f380-3440-b21b-2d341d7597e1 | -13.67001 | -46.5219 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b360c790-e3a9-3a80-a0ea-b863f0244df3 | -10.9494 | -50.25137 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cac64f55-8123-3641-9802-3952670eb9d2 | -15.229 | -47.94054 | 2025-10-28 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db738b9b-8f7c-364f-bd5a-17a41a0bf126 | -10.83377 | -44.95885 | 2025-10-28 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e73cdf8-f732-3e70-b40a-92ff59c883bc | -10.56233 | -49.76312 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8482167a-2f5a-3c15-8dbb-9e06629c9505 | -9.57928 | -46.95211 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4419aa15-7fd5-3ce4-a2bc-afa35a0283a4 | -12.19069 | -43.58277 | 2025-10-28 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 332966ce-1ecc-3bf8-8e8d-61a781cf197d | -9.62628 | -47.71727 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69524402-2315-3b9d-ad7a-d0a4a59e6366 | -7.93135 | -49.73729 | 2025-10-28 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08f30866-bb75-3904-9183-7f4c340b14e4 | -14.53407 | -48.00206 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f37f9da-3d54-3465-9da0-e387a103b680 | -10.56295 | -49.82485 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07d4ba6b-5a4c-380e-ad95-0c4cf143f2f7 | -15.16897 | -47.22282 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27d3dba2-e6eb-3108-9600-56a1a0681d75 | -10.95165 | -50.273 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4552d0e7-ab00-33f0-b432-c23a43571dd4 | -9.97477 | -47.16964 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa09bac6-817e-3f05-ac4f-1cefc928e14b | -10.9511 | -50.27652 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06527f99-8c55-386d-b6ea-8823c62419c7 | -15.16828 | -47.22765 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b58f7ec-4849-33e1-838d-fb655614ea7c | -15.57795 | -43.20605 | 2025-10-28 04:44:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 9ee58fc9-1c7c-30fa-a807-eac79a88fdf2 | -10.64339 | -48.0149 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af625b0f-8bbc-3e71-81c8-b934a89a165a | -10.92168 | -50.27577 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9996fe15-be10-39d1-a553-d78b4e7fd707 | -10.36164 | -47.14437 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dc01348-87d0-3985-a61c-3607853d0fb9 | -10.94275 | -50.27195 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11172d7e-15cd-3020-9ded-5e1a43877ea6 | -13.54723 | -47.16721 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78aa9f54-88a1-3ced-b9cb-faa546e905ed | -15.31312 | -48.05543 | 2025-10-28 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b52ac95-84a5-3879-af19-c6e9c5054b6c | -13.23833 | -47.06741 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74966ed2-b94a-359f-a228-f17158621377 | -8.94915 | -44.95237 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5170b33c-af69-3732-ad56-3a652bde2c0c | -9.57009 | -47.89783 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd3e43b9-3baf-35eb-a35f-65b9be1b9e80 | -9.04117 | -46.91899 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b6429d7-a845-3249-bcba-ecaa4c12e225 | -13.7876 | -44.34101 | 2025-10-28 04:44:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80a5edea-2a27-3013-a35b-e53db7c878b4 | -13.90293 | -46.65265 | 2025-10-28 04:44:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3103ef59-c2e8-3090-95e3-77b0647e3592 | -9.01358 | -43.97631 | 2025-10-28 04:44:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0eac8ccb-99fe-3b89-b2a8-8391e07d737a | -10.36218 | -47.16613 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e925eef0-405d-391d-be9c-ff9361743c0e | -10.72601 | -48.13326 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4707edf6-8a43-3b87-8839-cfd88e6d690d | -12.63242 | -45.07948 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24ce708e-3b19-305d-a9ce-4596e19538c0 | -10.79793 | -49.66178 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4c7b2a0-c90e-3328-a0de-ce53fe46b5f7 | -13.86385 | -48.51732 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7685a4cc-4626-3b58-b29c-655e48779622 | -8.63019 | -44.78934 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dde66f0a-d8c2-34e6-ac97-6bce58965521 | -13.63034 | -47.03787 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d2b5f36-108f-3e48-a7e2-8464ee3827e4 | -10.75954 | -44.7518 | 2025-10-28 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a792322-2119-38a1-a051-0cdfdd8f3e62 | -13.73957 | -48.43238 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a116cfdb-3b53-3916-8f94-52ec08b55084 | -12.37402 | -51.48523 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d0204f5-269b-3569-9191-75e1072f12d6 | -13.66736 | -46.52 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1f9be1c-bfbc-3dc9-8492-382c54c12c6a | -8.25256 | -46.89377 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 651f94a1-e701-3717-acd9-6d8c1ed2ddc9 | -12.38531 | -44.9673 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 993c8522-d825-3fcd-a6fe-a244a3dfc94d | -10.91835 | -50.27524 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24fc354e-fcf5-339e-b0c6-c5114e0c93b2 | -9.53923 | -46.94589 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1313e7fa-e64a-3283-8ee4-e247eb2cf1d2 | -10.29786 | -47.1749 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 023eeb5a-877b-32b5-887e-25fa24fc1067 | -11.71397 | -44.44677 | 2025-10-28 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6c33601-40f0-3e9b-830d-821b8bed6ef4 | -10.91069 | -48.00823 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3758b408-1901-3c79-9c1a-91e90b2b798e | -10.92389 | -50.2617 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b4283ef-e89a-327e-be38-c88f13a75c7a | -10.93387 | -50.26331 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d83a768-c4e7-3e24-b65e-924b06c620ed | -9.9931 | -48.10551 | 2025-10-28 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 061171d3-2a18-395c-8cdb-10ae1cbf04eb | -10.54254 | -50.02042 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ad98f26-2156-3e24-a13e-e768d5e05231 | -14.73626 | -48.16908 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb4a00be-e944-3a28-a5e9-d04f82ce4b4a | -9.47515 | -46.90339 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 397bd28a-482b-3132-adc7-aaaa1c05e6fd | -8.14488 | -47.75118 | 2025-10-28 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f517b40-c910-3899-b4f6-142f2ab0eba5 | -12.09124 | -45.68034 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2579a31b-a91c-3988-b19d-e49dcf619958 | -13.55926 | -49.57897 | 2025-10-28 04:44:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 725aeec9-ef5f-395c-9eb4-03127417bffb | -14.76799 | -44.96074 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1fd7fb5-5ad5-36db-9558-1437dfc50e37 | -10.87072 | -44.40963 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9684b51c-9150-3c61-8361-369ee8ea7a6c | -14.31546 | -48.0197 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64f2f931-f8e0-3127-99ca-33c1ed1fafab | -9.22352 | -46.36566 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 805eb06f-e53e-347c-8cc0-8b2249dfaacb | -9.97353 | -47.17799 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79ec5896-2e63-36e6-b664-1e98e0cd22a6 | -13.36311 | -47.66803 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee9e41f8-3488-383c-89cf-12d280ec9f30 | -13.67139 | -46.5118 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb4cfe92-132b-3292-9bd2-a42c4f94dc50 | -10.57016 | -49.80063 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f6f2f3d-08f9-3493-ad4b-c45b313f310a | -14.54324 | -47.98505 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b516983e-b4f0-3111-9a46-bd4d438dce4f | -13.61588 | -47.02998 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75b1be87-5339-3ee9-98f3-435d5a4ddf19 | -9.55164 | -47.8076 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b14383af-eb6c-3127-b376-926803b9d4a0 | -11.14514 | -44.94165 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abe3171c-9df7-3b55-9e70-00ed0f702001 | -10.93111 | -48.03983 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 425e8038-10d1-34c8-affa-81e09eb9307f | -15.15378 | -46.6044 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e7413df-8593-3c5e-a5be-972d077a8862 | -13.6228 | -47.03617 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e68d241-091a-3e42-a9f4-38aa1b950693 | -9.5579 | -46.97069 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca17dc98-531e-3977-b0b2-96bfd9d8f8ed | -10.61937 | -49.01469 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3987a74d-af8a-39f0-b453-33301c3fca3f | -14.4214 | -47.8538 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ae5d687-9a57-3493-8989-22644c745059 | -9.54148 | -46.98116 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c65a75cc-2317-30fc-b1fd-739acf6a6440 | -9.55413 | -46.99613 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be6ae414-88a0-3574-9182-4b95720c34e8 | -10.89401 | -48.37923 | 2025-10-28 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e5fca86-5930-3b13-ab5d-39a296ffe2ff | -10.8678 | -50.14081 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e35a54e-34fd-358b-83af-52792a57c0db | -9.25347 | -50.02304 | 2025-10-28 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb2c0fad-c21b-3360-87ee-93ef1990cb42 | -13.3026 | -47.07548 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36ebfa9e-2ef6-3afa-958e-0be6b744ea86 | -12.24399 | -46.52327 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6b215b8-d12b-3ad6-a4a1-5de835d8bc51 | -8.05531 | -54.92714 | 2025-10-28 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75a50363-a21c-3126-a02e-747a5ff5cc8b | -11.31489 | -51.45744 | 2025-10-28 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c8ca398-9cb1-3dee-9d9e-1d58c76f6d60 | -13.66864 | -46.53201 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f36c7e91-0e1c-3628-ba76-53873930881e | -10.87632 | -48.62871 | 2025-10-28 04:44:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f37522aa-4f91-3a5a-b1e9-9f4c725211d5 | -10.94722 | -50.27951 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65ea2035-e2b8-3162-9c24-88d8a6ff67dc | -7.12845 | -55.11241 | 2025-10-28 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b3fd050-5560-3fca-86e1-2e04bad8893a | -14.42935 | -47.85077 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README58.md)
