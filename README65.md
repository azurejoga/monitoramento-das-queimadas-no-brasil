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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a177d76-592d-3e4f-8a4e-e2baa012d4e8 | -11.61333 | -52.14286 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0ab10237-81c1-331c-8133-3f515c3b58a0 | -6.23851 | -42.42673 | 2025-09-03 04:46:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 67e5a11c-947d-3895-8b5d-fff2bbded59f | -11.051 | -45.40526 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4fb83b1d-b1cd-3351-a591-fbfb45e6df11 | -7.69585 | -48.74818 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 13ccf149-d045-36fb-9c0f-43fd4faeb090 | -8.05728 | -45.36451 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ef904b1d-8776-3984-a7d0-36eda6bd2355 | -6.79946 | -52.82759 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d53bda-33b9-3f1c-bbfe-a4104e2eb327 | -6.82309 | -52.83137 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 469bd68c-1a0b-3f8f-8357-a35d3ecd1473 | -6.61768 | -53.12937 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34cefb2f-8bb7-34db-8acb-4bde5e18753a | -5.94048 | -43.03895 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 15eb9924-6a6a-37ca-95b4-5c0f9ebad700 | -6.25003 | -42.62159 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f352f4b5-85e1-3c16-82d3-5aaa2d9f5a8d | -6.53919 | -44.56557 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99c034dc-2c7b-3a8a-95a9-5b4d4338129e | -6.47729 | -45.41518 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| df253b64-863b-372d-84c9-de1520ff82d9 | -8.8278 | -52.0096 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efff2113-a0e7-3ae5-bc0b-6e555d8d8972 | -6.35337 | -45.6478 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cd1b906-a65b-3abe-86c0-4ec0067e5a97 | -6.46879 | -45.4149 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 12430f58-57b8-39da-a9ed-19697d3204fd | -6.83091 | -52.84748 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45f8a939-9846-386d-9589-0f42fa941805 | -10.0431 | -56.09927 | 2025-09-03 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69ad08f4-1d00-3846-9fdb-2ca0b24c0576 | -9.64905 | -48.07512 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 83418f8d-5f30-3d5a-844c-a69e0e6b33a4 | -11.13991 | -46.3455 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d4f7e42-f934-32ba-bb94-ae99899ee91b | -9.60212 | -47.8422 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0231cb56-d0df-34df-8c4b-76efe982e20c | -10.05724 | -48.0914 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40a4c84a-75e8-3560-8fbf-8a81501f48e3 | -9.95413 | -51.63729 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 260567cc-cea0-3de9-bfad-328fb0cf9d13 | -6.23428 | -55.63148 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea0fb037-9bed-3949-94dc-99a607d99a0d | -6.97248 | -44.35374 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33efe54d-00e0-3f4a-83c9-bffec716dcab | -8.08027 | -47.60926 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f22eb153-dba0-3a9b-87d3-5eede52a8498 | -11.62863 | -52.06626 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd22e9d8-4758-33e4-973b-117dde32bfb2 | -11.90941 | -50.62283 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dac7bc14-2365-3420-85a0-0f29727f804e | -10.95843 | -50.76527 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2fcdb1e-4ed7-3a9e-a5d6-9f521240522c | -8.02644 | -44.05004 | 2025-09-03 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 501c58ab-8573-368a-a6a4-be9bd8aadcea | -11.59292 | -52.12164 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 24818294-8387-3127-8193-ad43967e1430 | -8.05404 | -52.36438 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9fea67d-a2b3-3713-9864-9297bc8fd24a | -6.81923 | -45.6815 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 963f8be7-af6b-366a-8e39-9a28ff6ad1e3 | -6.30076 | -44.84801 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85491c26-2a5e-3778-99e1-22b1d06aca61 | -6.95257 | -42.97627 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 52a07d36-d653-3494-ad45-270f3fde1b9f | -6.58705 | -45.90545 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15cdcabf-8175-3ae4-b4e3-2ca8880e66f4 | -11.06709 | -52.0696 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 514d2248-1e6d-3a89-b577-9ffac595ca70 | -10.12742 | -47.44093 | 2025-09-03 04:46:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c30db678-02fc-33cd-ae51-46d3547cdf48 | -9.77354 | -49.97775 | 2025-09-03 04:46:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f97c84a-4f5b-3038-a714-22ad94950c34 | -5.89553 | -57.73755 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3591214e-e48f-36c2-846e-d7b95719003e | -7.89982 | -46.46208 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59a7edc0-59e0-3245-9106-a92e15e24f2d | -11.5935 | -52.13969 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| a7f555ec-f1c7-362b-a470-4d50e4ef2347 | -7.13453 | -44.57104 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7047ec8-1f63-3016-a194-ed80e75708cc | -9.96236 | -51.62787 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d8c0022-b5ee-30f5-abcd-84a54617d2a0 | -6.85361 | -52.79158 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a12556d-f1ae-326d-b79e-bb3701afd6c0 | -8.02496 | -44.06071 | 2025-09-03 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a6f424c-bb78-32aa-bf0f-91f4918d788b | -6.82284 | -45.68601 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08287bf5-5558-30bc-9b10-1550fa9204c6 | -7.59737 | -46.22382 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c3e0d09-6e40-3ee2-a9e0-744e8c5fb315 | -7.49306 | -44.81126 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4822a9c7-0872-333a-a3b0-4fab66963075 | -7.92459 | -44.93891 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d00a2fd-b840-3f5f-8b61-551ca36eaf73 | -7.48609 | -44.82809 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96367f65-047a-308e-aa1c-2044cf566c46 | -7.92464 | -46.43321 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60cdf718-a476-3211-b61f-7b168339a74e | -10.95438 | -48.14887 | 2025-09-03 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 146f4b82-111f-3628-9bf7-16dc358b5cbc | -5.80686 | -43.23943 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d359a046-298e-31d9-be19-a58ff70b693f | -8.01336 | -50.09214 | 2025-09-03 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e23b0d5-9dc1-316e-b492-d462d3d82710 | -8.36614 | -48.30306 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1cc8c78-6f6c-3f83-93cf-0c5b5cfe9c5f | -11.67882 | -52.2041 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ececf3c-898e-3f7b-b477-7d4207e364a8 | -11.64073 | -52.05382 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc06c4e8-cb89-3fc1-908f-6ebc7ae025a6 | -5.86702 | -57.7696 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 608bccc0-551e-376a-8725-2c634378d172 | -9.65345 | -48.0712 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6b4834d-a287-392f-a252-17aa8f4f2f89 | -8.34038 | -52.53298 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3d91828-22ae-3fb2-bceb-7f8be1185f19 | -10.08678 | -54.76437 | 2025-09-03 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ec36a77-2781-3715-a15f-d5d21c0b739d | -6.64674 | -44.09999 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebfd2ac1-82d1-3871-b127-e0354c840456 | -6.77932 | -52.8021 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8ee5213-31ea-326d-89d0-92160c635e16 | -10.84703 | -47.4509 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8192322f-ea2a-377d-8137-83a2c8a14606 | -9.95467 | -51.6338 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a6419dd-d65e-3877-853c-7d5fd091073b | -6.53984 | -44.56105 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d5e5c93-a177-35aa-9523-ce51976e615d | -10.45818 | -54.77901 | 2025-09-03 04:46:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63266c01-74fa-365d-9fab-bf362b6399dc | -9.74005 | -49.40738 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 118c958d-cde0-3b3b-af40-4c45b703ff41 | -9.15403 | -49.64648 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d789adb5-54e1-313c-9bf1-9a7a12e77a75 | -10.45883 | -54.77502 | 2025-09-03 04:46:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60e859ae-4162-3208-846a-05f772d2786b | -9.95629 | -51.62334 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4aa9df8-662e-3705-8af4-ddb41713adfd | -11.38634 | -43.56576 | 2025-09-03 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6be58cb2-0276-3d76-b8ba-3a5b29a4a4cf | -6.97208 | -43.23922 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9d3f1157-0c6f-35a8-804c-27d9a97dbb61 | -11.09069 | -52.02684 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30466cc1-1edd-3f98-9930-0bb272716f2b | -5.91123 | -57.72634 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 71717669-c10e-3688-aabd-96ce58e09339 | -6.09936 | -43.29018 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5e6d03d2-b29c-320e-9ea6-d2a4e32bf881 | -8.72057 | -46.13632 | 2025-09-03 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fd2f6b9-07bb-3327-b401-77d77e4c5a6d | -8.08416 | -45.50177 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50ffae07-314b-3deb-999b-c226d3653c77 | -7.66832 | -42.71646 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 041541e4-c36d-36cf-a916-e1b501fa07e8 | -11.59456 | -52.11113 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53f7e914-e001-3230-ac74-18b8402ffa06 | -5.87379 | -57.75697 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a3733430-e0e9-3a2a-ba66-66b89990d8a2 | -7.78239 | -50.97227 | 2025-09-03 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44da5b2c-8098-3a82-8c05-0c32eb74ea9f | -7.90587 | -46.44877 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b03f919-643f-3c7e-9bcf-b25025fe2093 | -8.36428 | -48.31573 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3634c263-25a0-38ef-a4d7-448252138a8d | -8.06164 | -45.36507 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 933f9f6b-8ffe-33bf-8d0c-76b096833720 | -9.81299 | -54.88182 | 2025-09-03 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbe2c3c7-ed80-3224-8343-05a10a85d88c | -11.94114 | -50.59713 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e70967af-aca5-307b-a77a-80314e7ccd68 | -11.68754 | -52.14802 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2efc79f-498d-3a07-be06-dfc11119b045 | -11.21245 | -55.07328 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7d1bb80-8d62-30c3-a655-dc131347c074 | -7.72017 | -50.24989 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83faf16a-0827-3b78-9b53-8ab3bb6adf09 | -6.87461 | -45.56931 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8395ed70-30ef-3b1e-809b-ebcc77c585db | -11.6766 | -52.19656 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44979b08-720b-36c2-8f75-f34d0a334390 | -6.45154 | -44.6777 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 957b1d39-f337-35d5-950d-fd3a94f022f8 | -5.87598 | -57.77131 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 578ccd26-5c05-37d3-858c-affc179fc032 | -11.60662 | -52.07711 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c58707a4-ce99-3fd7-9882-4282bdf2f409 | -9.64972 | -48.07063 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c24e7424-47c9-3b89-beea-504616af8e18 | -10.13675 | -46.29939 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 230bf348-2763-3d79-aad8-386fcd889c95 | -11.6044 | -52.06956 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2351495-ef69-357d-a04c-cf39cbb8800d | -5.7979 | -43.23231 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52b03748-71c0-3081-aa2f-d5e971c395b9 | -5.91422 | -57.736 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |


[Clique aqui para ver as próximas entradas](README66.md)
