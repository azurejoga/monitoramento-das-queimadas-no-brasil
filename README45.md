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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e72fbff-1922-30ed-b461-eefaa8e32254 | -12.33794 | -45.71499 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca584a8f-83fc-3131-a16d-840f04559481 | -6.73288 | -43.39026 | 2025-09-02 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 499ebb3f-3fde-3c7c-9b51-238707893761 | -6.82589 | -52.82851 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c052211-334d-37b3-9c49-3aa8b65af74e | -7.19809 | -43.2618 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 44b7fd96-736d-3aef-b850-c30288ca74b8 | -6.49015 | -45.13369 | 2025-09-02 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40cd43d2-42e1-3bb6-99f5-dec84bd1ce26 | -11.65825 | -57.36293 | 2025-09-02 04:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 27325f64-1d17-3b17-b7f6-d03eae2adcaf | -11.96208 | -45.85 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4db7af26-14ab-3039-adb4-f71ccfbd994a | -9.75269 | -54.76588 | 2025-09-02 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cc32c04-fe4a-3e3f-aeef-cff169b97b59 | -12.95374 | -48.08881 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 055cdeb9-cf9a-3769-b0b6-6c25019d8586 | -11.67284 | -52.18016 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 27dd29f7-b54f-39ee-83fb-e5d3a1be7dfb | -6.79015 | -44.62637 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b2ffec9-c229-3bf7-89bb-b566be59aa5a | -7.70554 | -45.01691 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 374f5015-4001-344a-b41b-ea551ff49270 | -7.69118 | -50.27375 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dd9e77da-c61a-363d-a4cf-1cb622d0c806 | -13.6916 | -46.94364 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e536f128-2fb1-30b5-b2bd-68c67e3c3aa5 | -11.08359 | -45.12529 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2adda42c-a4ff-3cf0-a59d-f804d9b0708e | -6.88163 | -45.86008 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ab8af94-0fb8-31c8-8172-415b8b13fa78 | -9.7581 | -46.9271 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b384f57-3dec-3e72-81ae-aae8697d8a58 | -11.65033 | -57.36763 | 2025-09-02 04:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 713322ff-c100-3395-810b-d780d9c8530d | -13.49598 | -46.9327 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7afca66-21db-3e0f-a4d6-57a2105a6c75 | -6.96247 | -42.07922 | 2025-09-02 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2f2b8974-e5c7-3722-bdff-2a180e5b9e97 | -9.7552 | -46.92239 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea29ee95-ed51-309a-9811-e46b1533a3a3 | -13.72384 | -46.93531 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f34ff546-ac38-388a-ad35-1fb570b092a4 | -7.06452 | -44.33772 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5cd8573-7847-3460-bee1-c0e4cd1b668f | -11.9609 | -45.79358 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e19893f-2a15-3430-89ba-466dd09e064d | -11.37367 | -43.56997 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 758255dd-368e-3d0e-b516-f38f5eefb87a | -9.7603 | -46.93608 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76e25fe7-7002-392b-baaf-4dc5a3620e06 | -6.98632 | -44.31773 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c69326c3-232b-363a-83ce-848f816efa58 | -6.79798 | -52.82689 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e561849-fa28-3770-9493-94d69169d343 | -12.59588 | -48.21021 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3038287b-82a6-331e-88dd-2ce17e4f4627 | -6.82654 | -52.82492 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fff019c-ff03-31a9-b874-634ef06723bc | -8.19952 | -46.78998 | 2025-09-02 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32e1051e-0cb4-360c-b5d7-798af073df99 | -10.05187 | -48.14466 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85f5becb-4a4a-3701-b7e0-56735ae54c90 | -11.65161 | -52.18734 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 01a822d2-4be5-322f-aa1a-c54bd9ea78ed | -12.88437 | -48.16507 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43c06a84-3b8f-3ebc-9c75-d2c87ccd9782 | -7.66926 | -44.74097 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b63fd0-39f5-3041-9ef5-1225bba468be | -13.52808 | -46.99544 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f2a7204-e509-358c-9e52-8fed3a2e3b39 | -9.73699 | -48.9756 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48434ab1-c119-350b-b9fd-a6836fb0b241 | -7.63097 | -46.55286 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45a8a1b9-6d59-3bc6-a636-ea918f679cc2 | -7.6105 | -46.03429 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e9e5f6a-b00f-3aca-93b1-64a4efd5cccd | -6.80323 | -52.82628 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3dce6647-d770-3fc7-9c52-acea97508844 | -6.96058 | -44.34994 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bdcb6a4-9ecf-38d7-b9da-217266df7e19 | -8.83989 | -45.78507 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21fddf5f-d800-35c7-aa49-8633cea8ff3f | -13.58567 | -46.92598 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8e2929b-c52b-34d8-8e82-6730e47741fd | -6.95554 | -44.35995 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aba42bb9-e24c-383b-820e-945f464ff106 | -11.71778 | -46.93406 | 2025-09-02 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92af7a89-83ea-3cae-9080-496293b1a703 | -8.81708 | -45.77333 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c848f4e-4b0c-31bf-be8a-1f428740ca81 | -8.83522 | -45.79205 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5969b488-7f47-3ab6-aa26-5a897b76b100 | -8.45689 | -47.359 | 2025-09-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85ed8488-2b18-3978-a050-3ae25b87708d | -8.70528 | -47.86877 | 2025-09-02 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d372b775-f4ac-33e6-90b3-c35bc83ef491 | -7.16606 | -44.91999 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8155b18-1db0-37ba-9809-3badb7770b6e | -9.68618 | -48.28324 | 2025-09-02 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4402e3b4-0cbb-35e6-a7dd-29671157bfa7 | -8.85932 | -45.79597 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17d8cdf0-f461-32a5-9792-9b96f9b4160c | -13.5296 | -47.00769 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19d9a5be-5952-3f24-b395-29b17825bfa6 | -11.66891 | -52.20171 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 19214ed2-4a34-37cf-b3e7-f99126b11446 | -10.05724 | -48.13614 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 25e872d3-93e1-3e54-97a1-02e4292e08a2 | -9.75858 | -54.76699 | 2025-09-02 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71ac9fd7-1764-3c25-8370-1ea7e22c0745 | -13.53024 | -47.00381 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ac312a0-7cf6-3d34-bd4d-89e5f69e7ae1 | -11.89963 | -44.88839 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 997bd32f-972f-34a2-ad57-2bc3636da951 | -11.91312 | -46.67957 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 173e7586-544f-3ff2-a905-a93c97939b72 | -6.88992 | -45.8534 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fff46444-ed4d-3048-b701-3a8bcc656a09 | -6.77171 | -52.81317 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d16b85e1-edad-36e6-a990-c951956bbb3a | -11.38257 | -43.62219 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6af4e06d-b0e2-3af4-8183-e521a5596e9e | -12.77088 | -48.08296 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c6bc225-3610-3a05-b19e-cb34d662ac76 | -6.17325 | -47.27689 | 2025-09-02 04:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e5168ac-19f8-3093-b3e7-d2f7fa186aa7 | -6.79837 | -52.82185 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3726e30-6285-3d94-97d7-e716cf3725f5 | -11.09158 | -44.62963 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1030f1ce-85bc-3cdf-ad1b-386138500f64 | -7.1009 | -44.76447 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aebd3cde-e80a-3aa6-9d27-8432d8b1f79a | -11.0564 | -52.06883 | 2025-09-02 04:14:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b3992b17-1a11-3345-9e34-b5483f758bdb | -12.67295 | -48.21738 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 295275d1-dc98-3d44-8dda-24142762ef9a | -12.9886 | -48.10458 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b8b4a50-aa55-3db4-aa21-02c71c3b47fb | -11.42735 | -55.183 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 751c4e21-497c-32f4-a921-8fea8b4f4143 | -9.64717 | -47.80837 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f21bdcd2-acb4-390d-a0a8-3b36c60b8a9f | -6.77718 | -52.81411 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6b09666-0eda-345b-b1bc-8650ac412ef9 | -7.60699 | -46.03372 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4341e195-677b-3cb2-bb5b-acbf0f58147a | -7.53437 | -45.35748 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6730c1cb-30dc-39f4-bbeb-bdbb975b1e7b | -11.91698 | -50.62362 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c2b6513-ceb5-34c6-b34d-fd98ab9f5dc6 | -7.46792 | -44.81241 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7c0f65b-7663-35e5-aa65-1b8caa8df02f | -9.68872 | -47.9058 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42fdc4a4-c9ca-3795-91e1-b26aada0b9a8 | -12.58488 | -44.80841 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 814864d4-eefb-3482-858d-254ef507d5dd | -6.42698 | -55.61701 | 2025-09-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a844cd2-772c-31f8-aeff-8576c18c68ce | -14.03871 | -44.61168 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8899c43-f4ed-329e-8bac-d3ae02826a23 | -13.71767 | -46.92989 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35e59c88-bc3e-3a6c-a973-e80ab5491d25 | -6.84292 | -52.82792 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 264cd912-f85a-3d86-ba9b-e7994ebee9ca | -7.53837 | -45.35346 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df67697a-a92a-32b8-82ad-4dc350483a89 | -7.99115 | -44.04663 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48b7c8ef-6f85-30fc-aea8-939c2bf04941 | -6.851 | -52.81433 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f697cc17-246e-3544-9790-41ce6f73dc4d | -6.77109 | -52.81669 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c312dc3-7e5e-3caf-a23a-4bed69544c9c | -6.85522 | -52.8222 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0f44eb9-c8b5-3c89-9cf1-7bd77c17ab01 | -7.49207 | -45.3581 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cc51a47-1a00-3041-bd24-2786c076ac04 | -10.33994 | -48.14246 | 2025-09-02 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6eb72f55-1213-3871-bb51-09b726ec53be | -12.85505 | -48.05126 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6755f23-29c4-3b78-b3f3-680ce966f0da | -12.57826 | -44.80732 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| daede8c5-4fc4-3a6e-89e8-f119a0d25f7a | -8.19084 | -46.79737 | 2025-09-02 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7d52d4fe-d33a-332d-8b19-528c2acc1622 | -11.88559 | -46.68297 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8ec51a5-5923-346a-9710-5180c8ba16cb | -13.70121 | -46.88492 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2df2d49-9eb3-3bd2-bd9a-449b1ba2f2b4 | -6.77223 | -44.61963 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09d4ecc1-ed3a-3230-b9ef-e6aa6425344a | -7.00266 | -43.53253 | 2025-09-02 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4dd12db-a613-3ab8-a61c-0a82ed11af6c | -6.79544 | -52.80641 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c603d980-95f6-3902-b843-293ad8845ab0 | -7.09862 | -45.34185 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0dc15a0-88cf-3bf1-940d-c3ad8504b0dc | -9.64953 | -47.79461 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README46.md)
