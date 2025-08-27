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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d6c90f3-1dfb-396b-b90a-06de314afd90 | -13.84266 | -46.69048 | 2025-08-27 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55bc3e68-9bb2-3e71-834f-66764b4eab78 | -17.77335 | -44.4818 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06b302b3-b608-36bd-899f-76ca11abca35 | -18.53046 | -48.91756 | 2025-08-27 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caa480e8-fc8f-3dad-85b5-219ad2489d60 | -13.66351 | -46.905 | 2025-08-27 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e9d0ea4-da18-33a3-abcc-f4a6d32f4e57 | -12.87595 | -48.10402 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c5fd29e6-2f54-3c9c-80cf-decdbafbfa23 | -13.41646 | -46.8627 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5713fce5-0abb-3ded-94c2-b2c85ea98e92 | -13.34703 | -51.80185 | 2025-08-27 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0ea1170-fa76-3be7-8ab1-2fb325379f1a | -12.76608 | -48.15487 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45fcd50c-1c55-3e7b-8111-0ee9e8158f60 | -9.40761 | -60.54868 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 088c6ffe-a588-3bd8-9d26-e0fca41611c3 | -15.45105 | -47.4381 | 2025-08-27 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f70bff42-ec4a-3895-a640-9ce4f3668ada | -12.79917 | -48.11671 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 18493981-ebdb-3cbf-a547-f584bc8d5b2e | -15.10543 | -48.54536 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ac76933-6cb2-3fee-a8d2-1c86d0b37f28 | -12.71475 | -48.13557 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64f69b2d-02e5-3b83-be92-b29ac924fbcd | -15.7923 | -41.47313 | 2025-08-27 04:27:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb896f21-e64f-343a-95ed-247107b45464 | -19.24594 | -42.05519 | 2025-08-27 04:27:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 295a1897-4c54-3b1d-b612-d95d7dfcbc25 | -13.42887 | -46.99748 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0115a33-b333-3281-aee7-34768ab049f4 | -13.50231 | -46.87601 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9f83230-071b-3a96-9a32-7fe58341f584 | -16.74008 | -47.59157 | 2025-08-27 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aeb9c8ea-65fb-3721-8089-c84856efe750 | -17.1529 | -53.50267 | 2025-08-27 04:27:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 724d2c4a-9a88-37bd-bed9-93edf00108df | -12.78162 | -48.12117 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33df72a5-ba0a-38b8-be83-f30857110983 | -17.9768 | -48.0431 | 2025-08-27 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| de201cbe-2e42-3e8e-8f02-3e0a74ee55e0 | -13.17486 | -45.28968 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1a94258f-7014-339a-a05e-cd5fa18a9a31 | -13.06863 | -46.33029 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f61e231e-a133-3e15-932c-5eae1fbb41f6 | -14.12538 | -45.40461 | 2025-08-27 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e2b4a14-e8f6-37e6-a274-9178d8f3eed7 | -17.55132 | -46.60975 | 2025-08-27 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0769e7a-4a5e-3c10-83a6-1e235505b456 | -13.46992 | -43.75004 | 2025-08-27 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0aba073f-2c1a-3746-8c97-fe1c5656636e | -11.82881 | -46.81351 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fd4422a-3d57-3177-9e19-19874ae7bc7f | -11.92288 | -47.12572 | 2025-08-27 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| baad88f7-61ab-3b6f-aeba-a80c08013393 | -16.78534 | -47.5649 | 2025-08-27 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 891a0cae-c266-3d95-a752-2021fca7a2f8 | -18.248 | -45.36128 | 2025-08-27 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 512f8c15-aad7-3723-a100-00960163d983 | -13.40641 | -46.8834 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a7d620d-3b9e-341f-aa6b-f291188e0f8a | -12.76384 | -48.16897 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b01f1390-919d-3aea-8197-0837d9040284 | -15.60895 | -52.7381 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fd93fba-28ff-39a2-9e57-40eb41d6a1e0 | -11.05672 | -52.02961 | 2025-08-27 04:27:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ba0c863-bc30-39ec-a7af-7ddacc02fd99 | -15.09243 | -48.62737 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6d19d29-86e6-337d-bd4d-3605d6e6753c | -18.27341 | -42.12971 | 2025-08-27 04:27:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 71f6d58b-b95c-3378-9d95-289b07b2af10 | -18.15816 | -44.4337 | 2025-08-27 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92af1471-ce84-32bb-9459-e3a5410e5ea6 | -12.65623 | -47.83993 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94f43784-b500-30ea-a108-082ae0c8a2b7 | -19.16146 | -41.50515 | 2025-08-27 04:27:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 965de2c5-9461-32d9-b833-8be08c4c1734 | -16.38095 | -48.81023 | 2025-08-27 04:27:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ac8811c4-d92b-3e80-b6a6-345878091033 | -11.79099 | -51.4051 | 2025-08-27 04:27:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0377f142-6421-3a6e-8c89-7b22ff3da270 | -14.12479 | -45.40866 | 2025-08-27 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1611cda3-12b6-3279-a486-48dd3befc470 | -9.63574 | -59.63737 | 2025-08-27 04:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3960fd0a-5ec0-3d5f-bab3-d64b799ec6e8 | -9.39159 | -60.52309 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82b84db1-706a-3084-84f3-c6047aa6d4d0 | -12.70357 | -48.18444 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c7f19966-bf5e-39e7-ad6d-b07a3cd0d5ed | -19.16084 | -41.51054 | 2025-08-27 04:27:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 40161f92-2261-35c7-8768-a16342732b82 | -13.3981 | -46.91514 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebad21bb-2f65-320c-abc6-c48bdd4466a6 | -19.46626 | -44.1869 | 2025-08-27 04:27:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1956015-21e1-3559-8664-f50cc98ad259 | -12.79754 | -48.10558 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0fd6ac8f-3cb8-34ea-81ea-70832f64b040 | -12.76883 | -48.15895 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9aee7780-a0e4-324f-afbf-6fa368c7e6cf | -9.41579 | -60.5436 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 526d20b6-1a07-3d08-ac7c-4e9dbdfc2c01 | -9.4141 | -60.51618 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f0e148c6-6951-3f1a-9ffd-bf82332ad4e8 | -15.61679 | -52.72177 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0aedea40-12bf-38ff-8244-0bf96d12bc38 | -15.6662 | -48.23938 | 2025-08-27 04:27:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9436400-4b20-3807-b18c-dc886ddc458a | -13.41256 | -46.86577 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ac6e923-4cc1-335c-aea4-4bb887cd6bd8 | -11.91531 | -46.73974 | 2025-08-27 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd30e724-8c27-3f0d-81f7-77d5858e5e01 | -10.77242 | -60.7887 | 2025-08-27 04:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5bd5c1d-62c4-3825-9894-47f567f3c682 | -16.03962 | -48.26047 | 2025-08-27 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 928ae41f-3cb5-3c5f-bd73-5f0191f28f3b | -12.77158 | -48.16306 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 6369a0b2-7829-3431-b46b-341cfb10e659 | -15.62506 | -52.73597 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b258a04-78e1-3f35-994f-47022718b69b | -12.79198 | -48.11916 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0d1faf6-b633-30d6-aeb2-7119c974930f | -12.89697 | -44.6414 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 53bdf632-c698-3137-8491-825921897e4a | -15.66012 | -52.73764 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dee6134-0dd5-3cb6-b8ac-600ec9513641 | -12.75603 | -48.1968 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1d7e0df-9ff3-3444-a0f5-8de9e5984fd9 | -12.70082 | -48.18034 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4e7ce7f-3ca0-310e-85a7-43e656410b9c | -18.5299 | -48.92119 | 2025-08-27 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62a4b147-abd1-37e4-a839-05c38507b25e | -12.76659 | -48.17308 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32d2b3a4-ea43-3cc7-8070-7f3a719838e1 | -12.25246 | -45.05489 | 2025-08-27 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a07dc357-510f-30e1-8a1e-a8ad288bbb3d | -13.40307 | -46.88286 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa8822fa-909c-31d7-9370-4a899b628ef5 | -11.80017 | -51.46934 | 2025-08-27 04:27:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69b1eb28-e6ce-3efb-8c89-bc689c0e0c97 | -13.42558 | -47.01893 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8f3cd0b-be40-3d4c-a688-ae95d5304515 | -15.98656 | -42.25357 | 2025-08-27 04:27:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 24c00a5c-e920-3c27-bed5-70087016755b | -18.21811 | -44.5264 | 2025-08-27 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34d5c71f-5721-31c7-a4c6-6b17b8d3b6d1 | -17.77933 | -44.49605 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5df98e3e-523e-350a-8145-10fc5ae39dca | -15.64114 | -52.73396 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b561b3bb-0db3-31ec-aef7-9edf963ad885 | -15.09082 | -48.61607 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99c32c07-8275-3a7e-9831-03b79e02762d | -10.52052 | -57.98684 | 2025-08-27 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71c47af3-a076-37cf-aec4-5a1897f9665a | -13.07312 | -46.32347 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ba6c0e15-5c4b-366f-8129-a393be7ecfa7 | -13.06464 | -46.30395 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91b53d5f-ac3d-3dc6-bfed-e99d18293801 | -13.40255 | -46.90849 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56947aa9-2960-362d-ae06-44b9928f96a5 | -13.39142 | -46.91402 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 089a0170-10c1-3cc0-ba6e-c518ff155ff3 | -13.43332 | -46.99077 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94bf75e1-9cb0-3422-bb8b-eac2b58cf54b | -15.61045 | -52.73571 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b0e5328-7275-383f-9178-3f76275f6159 | -12.75159 | -48.20335 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dc47d39-0156-3710-85a7-e58b686253b4 | -13.45165 | -46.98277 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9811968c-89b5-31ba-8766-f4cd28e9bd33 | -13.07084 | -46.31559 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 609a05ee-4764-3ce3-815d-7f6832a18b47 | -17.80576 | -44.50444 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37abdb3d-ceef-3a18-9348-6133f37f6652 | -12.77775 | -48.12416 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bfdf161-ae05-304e-ab28-d1e862f40f8a | -12.76603 | -48.17663 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70b4e203-3257-3a6a-ad29-85674f40d7d3 | -15.64026 | -52.73888 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d43efd0-48f6-3197-8cbd-a121df5519de | -20.00804 | -42.13932 | 2025-08-27 04:27:00 | NOAA-20 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 25f1dcf0-ef30-3fd4-835c-26c996493090 | -18.2517 | -45.36185 | 2025-08-27 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a37fbd9a-700a-317c-adf0-0bb39704a9a2 | -11.83269 | -46.81049 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77d997bb-45ae-3806-9b2a-647b0035d859 | -14.24258 | -53.3139 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e07723d8-30f5-3909-831b-05f4b27991d5 | -12.70025 | -48.18388 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 03921525-b646-3c16-a44f-14415e1ebf4b | -15.66233 | -48.2424 | 2025-08-27 04:27:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0de06d6-d820-3686-b347-199260f41073 | -19.40776 | -46.15883 | 2025-08-27 04:27:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a222a6b8-30f5-3bec-b98e-4e10c13337f3 | -12.25187 | -45.0589 | 2025-08-27 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b95d027-4587-3b5e-86df-83cceafb7052 | -11.05627 | -52.03283 | 2025-08-27 04:27:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 895719b5-cd11-3795-b94d-14c7dc4c7c1d | -10.51472 | -57.98557 | 2025-08-27 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README50.md)
