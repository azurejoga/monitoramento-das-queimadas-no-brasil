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
| 3e9c1712-663d-3547-90df-56bd73432d08 | -7.66126 | -42.71135 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ae93ef7c-4c5a-3489-8ae3-1a33b2871142 | -7.67585 | -43.87123 | 2025-09-02 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f777b1a6-bf04-3d97-9506-561885708178 | -6.82146 | -52.81869 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4917c04c-f466-301a-a8a8-fc23ac848724 | -12.75917 | -44.41441 | 2025-09-02 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0af6f7da-f34b-334a-af12-030f8e2ac2e1 | -7.61961 | -44.03376 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e48b15ca-2cc9-3e5e-88ad-8cbbc29c0b49 | -12.13551 | -47.19072 | 2025-09-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d9cb74b-f5ba-31d5-a2f9-f00315d582e3 | -12.94979 | -48.0903 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5e75bef9-0343-3b82-8b79-e10902ea85f7 | -11.8578 | -46.72201 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cce4b3e-29ad-3191-92d3-5d306a8f6061 | -13.70292 | -46.8914 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23f0de56-ce42-3c47-bdbd-582e38981736 | -10.26766 | -47.51555 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a33ad2d2-4ecd-3b1f-b66f-6c9996835133 | -6.81667 | -52.81387 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e36b7310-1cd4-31a6-a9db-bfe2981de753 | -9.48544 | -46.51297 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e2b9dc2-bd27-3d06-92a6-b98634e6f0e8 | -12.8543 | -48.05555 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d59f9197-2784-379a-8e75-d76feb1c6d3b | -7.53497 | -45.35377 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e066bc8-4b2e-3a99-88e8-d673681eadd7 | -8.13526 | -49.83382 | 2025-09-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dc73600-5da8-37eb-9551-4a7b9586dd4a | -8.54722 | -47.42351 | 2025-09-02 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17891381-9bc0-3e33-a653-d7517f6da401 | -10.06064 | -48.09333 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d649d39-3f76-373b-81b0-44cefa2a85ef | -7.38026 | -47.04597 | 2025-09-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 64c762bf-9296-3d1b-9585-9f0d5fe5725f | -11.01373 | -46.93861 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec675325-3958-326f-aca0-aef3b8f274fb | -11.63792 | -52.04671 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8d081d56-ca2b-33f4-a162-082dd14df04f | -11.67281 | -52.22652 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| b1840531-2ea6-341a-b498-429655d94b76 | -11.65941 | -52.17195 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| be52ca93-7227-3164-9ca5-4f13437e8261 | -6.79355 | -52.81722 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d4898bf-7c06-3ff9-b9f8-b6cef48abc81 | -8.12303 | -45.03224 | 2025-09-02 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 767ce79d-8ef1-309f-9785-9c72ee92277e | -10.04821 | -48.1203 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f5942dc-6082-3f3d-9d7f-151028a1ef03 | -12.62081 | -48.18954 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2a790641-f28c-3188-aaa8-619e9139e959 | -7.48341 | -45.36818 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39a3c71e-c142-394d-8599-63fe2b0463c1 | -12.61713 | -48.1889 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 41c28e2e-111f-3d66-a475-bcdc90c49fc8 | -13.28147 | -46.9137 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3f0b0d36-daa6-3ebe-9f78-898ec1402cc7 | -13.3083 | -46.83804 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f555d1a6-b7be-36d4-8e30-70d2b2b056ad | -10.66573 | -47.3321 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e499820-eab2-3e52-9858-67da5f9b07e0 | -11.9157 | -46.45535 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08640606-3da7-36f1-9925-2520827c4fa7 | -11.0927 | -44.6226 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da75a746-5bb4-3817-8056-62177d4016f3 | -11.9708 | -45.88152 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07b861f6-04b8-37ac-bc62-0c605cd9deda | -11.66618 | -52.16218 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afe9173d-c68d-3801-a316-2e30dbef19c7 | -6.81023 | -52.82156 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42bb9989-c4e4-38ee-8f6e-01c9394008c4 | -7.19478 | -43.26128 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e80a9c7e-93c8-3c1f-9a64-e07cb111795f | -11.96644 | -45.80199 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b581a0c6-9ba7-30c9-b739-d42b863de485 | -6.84423 | -52.82065 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e54c601c-02a6-3021-86d4-b6c90fdde5ff | -6.83813 | -52.82318 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b254db0e-5c53-3336-a12c-45e48310d89e | -11.84943 | -51.54175 | 2025-09-02 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 561e275c-5316-348d-822f-7ddc2f8c4f64 | -11.65292 | -57.35525 | 2025-09-02 04:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2dbb6183-19f7-38e0-af76-282de89c7306 | -13.48351 | -46.92254 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0be6a997-6dba-32bd-b09a-436899530d87 | -8.18648 | -46.77901 | 2025-09-02 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| a2158b25-cd27-3d1d-9a3a-fa7c54a5d049 | -11.35717 | -43.67601 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe42ee98-7c40-30be-89c4-fbd894a66057 | -8.30884 | -55.10405 | 2025-09-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef0a561e-36e7-3068-8a12-4c82b56a5f21 | -6.89349 | -43.83518 | 2025-09-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dec4451-e419-3429-a00c-e7abad904ee4 | -11.87515 | -46.75718 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a5b81cf-bdcd-33ab-9bf3-91dcd2d3cc0b | -12.75255 | -44.41333 | 2025-09-02 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 024e53da-a6cf-37f5-a708-5b8e15386c15 | -13.7204 | -46.93469 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a24fd35-b9f5-34bc-8ea8-610e4ae958d3 | -7.9834 | -46.45862 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 96cb6ea5-7a7d-3dc5-a5ad-2b8de4b36422 | -6.97742 | -44.30908 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2225a2e-db93-38a4-856e-c8217fdbdbe2 | -9.84634 | -44.68363 | 2025-09-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8187a445-4e8f-3534-b1f5-73e39af88801 | -13.65726 | -46.93718 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74bd7740-3ac0-3dcd-8e42-213b8761e43f | -13.50198 | -47.0028 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cca1d656-6a59-3c29-b9bf-205b05518ac1 | -8.8527 | -50.58268 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a634464c-9203-3a70-8941-0b8e8f7c3e6e | -8.13088 | -49.83307 | 2025-09-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5418404-e687-380f-8c40-d5a6f041d4cc | -7.13115 | -44.57741 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2af4dfaa-899f-39d0-bddd-73b8958cbb39 | -8.88159 | -47.97199 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e92f9d23-429f-3a93-9f49-1831dcb9b18e | -12.57646 | -48.25751 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ed29faa-8807-3d57-ac41-3506b9ab15bc | -11.10647 | -44.64288 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91ca9618-16d6-394f-94df-28e965731c87 | -6.83266 | -52.82229 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3bf7ec7-30eb-3170-8616-2b13cc3a1066 | -7.49147 | -45.36183 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b79ed4e-2477-333a-a5bd-69c95dd0ab20 | -11.96268 | -45.84634 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a946995-408b-3924-9344-52371f95a680 | -7.91491 | -46.45135 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0dae5a4-8301-3d57-972f-4794c0881fdb | -9.83028 | -48.61683 | 2025-09-02 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ac9caa4-9774-3f05-b7fa-c830942dfce1 | -11.01366 | -46.83099 | 2025-09-02 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0dfa2f7-f5f8-3899-89a4-d5ab9c9a2957 | -12.4641 | -43.20449 | 2025-09-02 04:14:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 241e423a-1de6-386b-93ad-bf93c8256601 | -11.66026 | -52.19447 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6c6f3d19-6d45-3ab7-9264-ce1160941922 | -6.04312 | -52.17684 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66a9b186-5db1-391b-8d93-8d3fb667186c | -8.86805 | -45.78566 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d40dde6-f511-3576-9cd0-768e4f3456d3 | -8.85187 | -50.58734 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| de06e279-6643-316c-bd30-2bcad9d3a8a8 | -11.66692 | -52.21266 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 72d3d52f-2d50-3658-bab2-f7c15503eeba | -6.83941 | -52.81608 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37ca2105-677a-3420-9016-26f181ac3866 | -8.01768 | -44.05087 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93e0faae-a9b6-394a-bd7a-f801b39e6d72 | -11.65344 | -52.20453 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 29457358-9fd3-34e6-9417-b0bb18865a84 | -8.4658 | -47.37438 | 2025-09-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e404f53-7594-36fd-9425-b7e978f55fbf | -11.91975 | -46.45215 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b867b0ed-f328-3f03-8109-1dc42078e577 | -11.6714 | -52.18139 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| d519db55-c7e8-394b-a60f-336ad46a8391 | -11.05813 | -45.38927 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f324a0f1-6513-3233-af14-4f9519ead8fe | -9.73175 | -48.98203 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 49a946cb-bdd9-32c4-b5f2-22475f519147 | -9.64342 | -47.80773 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee6c3db-2f24-3f53-b1af-92232a848382 | -10.04645 | -48.1534 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 967ecedf-8f77-39b3-bb7e-f4e26518e3d7 | -13.53627 | -46.98891 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be12492a-65c8-36c1-97cd-85a6b254ad3d | -11.245 | -45.00951 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfeb43b7-b09f-3aeb-bfd8-286a7a01bbb2 | -8.28775 | -46.30331 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f909b12-c089-3b79-8a87-96f2218928c7 | -6.6866 | -44.04583 | 2025-09-02 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 219443e4-56f0-3feb-bc55-3fd004ea3268 | -6.35087 | -55.55935 | 2025-09-02 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b2b87cc-91aa-3fb0-b5ec-b8bde299360a | -6.8746 | -45.85892 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2226d578-d7ad-378c-9f9b-6ff91334f13e | -7.70361 | -50.30924 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 813686e8-5180-3e4f-8bdd-ab27189449b4 | -7.31911 | -44.29839 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a378844-0645-37e6-a012-e2002cee2310 | -7.98069 | -46.4752 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 70637947-0fff-3b4b-a98b-80e15503290f | -11.09102 | -44.63315 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc7806f7-c262-3891-859b-c28f827d2be7 | -11.6699 | -52.19627 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 14e5c225-c88e-3cb7-8335-a3fa91629ddd | -11.66706 | -52.18455 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3d4b5b6f-6170-3be4-a31c-06ff27070f1c | -6.99376 | -43.22207 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52e49001-aef3-3f14-86ea-d036d9fca358 | -11.6526 | -52.18191 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f8d100c9-1a64-3592-bb47-7ff3547d3914 | -7.53776 | -45.35716 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b84aa3e-72ea-30b0-aa20-53ea3acfd9f0 | -11.92205 | -50.62024 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 267dad8f-dae3-3a9f-8d20-e61568a8b674 | -7.98918 | -46.46816 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README47.md)
