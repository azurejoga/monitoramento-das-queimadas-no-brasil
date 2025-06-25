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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62d542ce-37ba-3578-82cf-b74dd8fad6b3 | -6.1792 | -48.0494 | 2025-06-25 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| efd5a25e-2d0a-3a1c-a2ee-909057e3f9f7 | -6.1791 | -48.0712 | 2025-06-25 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| c45a6001-f526-36dc-8f81-d337bbd8842c | -10.443 | -47.945 | 2025-06-25 03:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| bdad33d8-16b4-38e8-8d31-2b665773047c | -10.443 | -47.945 | 2025-06-25 03:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| f7ad184b-c174-3671-8352-3b8fa13ec591 | -6.1792 | -48.0494 | 2025-06-25 03:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 16c57225-7648-3a38-bd38-f7086ff89ac3 | -6.1791 | -48.0712 | 2025-06-25 03:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6ace57e5-61f3-350d-82c7-7044b0d623b2 | -4.5429 | -48.0151 | 2025-06-25 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| ec17d4d0-1e34-35b4-a317-22dd90251b09 | -7.01996 | -44.56179 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 805b3c4c-aba7-3d34-8b9d-e85e4eebb43d | -7.20344 | -43.10221 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b7aaa6c4-5acb-3d31-ba15-6f56c78d3313 | -6.22547 | -43.36576 | 2025-06-25 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 668167e4-f416-3872-ae70-8581ecc5eef1 | -5.50368 | -35.59586 | 2025-06-25 03:45:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be379a53-209c-30ef-94f4-933d6db27bfe | -6.34559 | -43.78614 | 2025-06-25 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0ed6c3b-c78c-350d-8c3e-e760234429a5 | -8.05896 | -43.10945 | 2025-06-25 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 93b403d2-8647-38dc-a47c-32e254427d4d | -3.61561 | -47.53792 | 2025-06-25 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 92662923-3d4f-382b-9883-a3e139f21de9 | -5.75967 | -43.39694 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a68dc455-3d5e-38dd-9caf-a3128913a52e | -6.91348 | -43.97596 | 2025-06-25 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0582b179-4a0c-3811-9aed-c6dde957df2e | -6.90993 | -43.96587 | 2025-06-25 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf1e2a6a-54e6-3338-8b7f-49bf5323b05e | -6.60491 | -44.26175 | 2025-06-25 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d36cc19c-1111-34e8-86bb-1e9ef57ac346 | -5.76304 | -43.39894 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a31622d-587f-3baa-b2ac-8a9807ded2c3 | -4.53518 | -48.01348 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6b0669e5-70f5-3523-94e9-f3b747b2bb5c | -7.02473 | -44.56602 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34fb23ce-9104-3d3e-9bce-f4947452ee96 | -8.24488 | -44.95426 | 2025-06-25 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7a0ac19-0bb4-36ca-ad74-0ccb5a056417 | -6.21944 | -43.37067 | 2025-06-25 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecd924e7-238e-338a-bc5b-9eb63ccea3c9 | -7.2101 | -43.09237 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d0451555-f7ac-3822-b37f-22f2b5098831 | -7.20787 | -43.09278 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 0b2cbc86-a028-3463-9189-1d29721a2bf5 | -2.44892 | -47.5001 | 2025-06-25 03:45:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5781eebf-f5cd-35aa-91e0-333159418096 | -3.61487 | -47.53875 | 2025-06-25 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a8cabf60-ce56-3f86-996f-efe77e61560f | -8.06462 | -43.10515 | 2025-06-25 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b716de6b-1db5-3d57-a387-e1cc3438b969 | -6.17377 | -48.07215 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06c5d13e-28d2-34e5-afa9-1cd6848bb2a1 | -6.95917 | -42.81146 | 2025-06-25 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a067264e-5da6-3abe-ade5-8703a473e274 | -6.18272 | -48.06138 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9b633490-aedd-3774-9138-500684ed80da | -5.35544 | -45.11993 | 2025-06-25 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b41ceb0-f8ea-3d51-a747-9a55aec7f057 | -5.91921 | -43.47817 | 2025-06-25 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11d15e62-3d73-3d34-acf2-97aff8e6d28e | -5.76355 | -43.39602 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c4b2dcb-833a-3d67-962e-6e1a3d3c2d1e | -9.0038 | -39.88358 | 2025-06-25 03:45:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3c7c457-434b-3981-8403-81fe8ca15c25 | -4.19146 | -38.36588 | 2025-06-25 03:45:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 73df3daa-df2f-31ff-9e3e-21b894624f8b | -7.61874 | -37.18256 | 2025-06-25 03:45:00 | NPP-375D | OURO VELHO | PARAÍBA | Brasil | 2510600 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 26b73833-285e-323b-a20a-293cae6c0b99 | -7.1986 | -43.10136 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fb6861f1-730d-31bc-800a-33ba94784815 | -6.90833 | -43.97501 | 2025-06-25 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 015730cb-63f0-3bfb-aced-2d195ada8b25 | -4.95318 | -37.44001 | 2025-06-25 03:45:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 24bef6b7-c625-3e78-ba07-5f74db88b8c8 | -6.17608 | -48.07038 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| eff09933-34e3-32b8-bf3c-ae12c01137b2 | -7.19284 | -43.10583 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4899f869-ca00-342f-9b7e-4c3dd37ce71f | -6.17601 | -48.05994 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bb87ba27-9b1c-337e-970e-cd5c1cd4fe49 | -7.19768 | -43.1067 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bbdb56bf-9393-3e69-8ffa-37d06dabe759 | -3.78405 | -41.04112 | 2025-06-25 03:45:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a025fc51-efa4-3dc2-8098-9a7dac259e7c | -5.35462 | -45.12008 | 2025-06-25 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7435252f-d032-3daa-a655-830d0a66323c | -7.20527 | -43.0915 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 37461ee0-f02c-352c-b903-e4f37d04ee6c | -4.53627 | -48.00722 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b572c7c2-e365-3574-89c8-f7ab7f485277 | -7.01035 | -44.55367 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea0dd3ab-4265-3a9e-96b0-fda1a120fa96 | -6.96007 | -42.80636 | 2025-06-25 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a5cec81c-4e2e-36fb-a8b6-2d57b1a4779f | -8.0645 | -43.10248 | 2025-06-25 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1fe830c2-1d2a-343d-92cb-79281d5995f6 | -5.91817 | -43.48418 | 2025-06-25 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c73d0ea1-5a18-3efd-b084-96b8303cca2d | -8.87086 | -47.27326 | 2025-06-25 03:45:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f33e631-a340-3edd-98cb-e4eaebaebe80 | -7.20692 | -43.09811 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a644dbdd-2de5-3093-a60b-145db748adb5 | -5.75745 | -43.40105 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3647d05a-7608-391b-b57c-48d34f377943 | -8.06357 | -43.10761 | 2025-06-25 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b6c67c93-c10d-3b71-88e7-9303574bffb1 | -4.54278 | -48.00823 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c5741b4-067d-37c7-a755-bd4ad6ab4437 | -7.20112 | -43.10262 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 78affbf5-9b2a-3135-b4e8-63109c2dccde | -7.02417 | -44.56919 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 259fdf50-d00f-3923-b8a7-1553f8c2da78 | -4.23207 | -43.63986 | 2025-06-25 03:45:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc84e5ac-2ab3-3e92-8b14-c7845db34300 | -9.54627 | -40.35127 | 2025-06-25 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 45b2b565-2eb2-38f9-8b4a-ab723f8efb30 | -6.29236 | -44.23807 | 2025-06-25 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c8b1851-2763-3d32-a3c4-10bcd7013ff7 | -3.61593 | -47.53262 | 2025-06-25 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de9812d5-02c9-33d7-9178-69e27c2d6d06 | -7.20304 | -43.09193 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| cdbf252a-4683-31f1-9179-7c15a9f55b6e | -6.1804 | -48.08443 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4f50955f-910d-38fc-8725-56abe358691c | -5.75411 | -43.39905 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 799b75c0-91f1-3d6b-9dfc-a78723d4c753 | -7.19533 | -43.1071 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c5b81ba0-23cb-3a8e-8b17-d2a627ee137b | -3.99352 | -43.24258 | 2025-06-25 03:45:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d032b16a-6610-368b-a6e4-065e527bf7f0 | -3.99868 | -43.24345 | 2025-06-25 03:45:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e63ec612-b276-3d6b-ad58-c47b9b0c380d | -5.73192 | -43.49933 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| baf8030b-06db-33d0-a77a-bb7752362eb6 | -5.75797 | -43.39811 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 390facd1-78cb-308e-9acc-f39096a8cad0 | -6.28706 | -44.23708 | 2025-06-25 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0362964-4565-3379-a39f-0d3a51bd4f99 | -9.5092 | -45.44045 | 2025-06-25 03:45:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05b395f9-f940-3135-8db8-9be47b11b292 | -5.91869 | -43.48118 | 2025-06-25 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14d2508b-abb1-3a96-884d-72a0309486d6 | -7.02359 | -44.57248 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93d4383b-98a8-3182-b3df-da37925fd26f | -3.78604 | -41.03875 | 2025-06-25 03:45:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d37b829-9243-3ad6-bf0f-0aca71c77099 | -7.02892 | -44.57362 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a979d13-1622-333d-8ab8-51c8e0896165 | -7.02831 | -44.57708 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a67bc74f-2226-383c-8d02-e8377acf65cf | -8.53696 | -46.33 | 2025-06-25 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dadcb5f2-9e96-370f-8698-b0e6069ee68d | -8.05985 | -43.10428 | 2025-06-25 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 953b58e2-a501-3dab-b661-4512c7e13b38 | -5.50423 | -35.59237 | 2025-06-25 03:45:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af59511d-5afb-39f7-98cc-36b060980d09 | -6.34503 | -43.78928 | 2025-06-25 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15b3b0f0-58e4-3038-a4d5-987a88d1a38d | -8.24428 | -44.95762 | 2025-06-25 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d48aafc0-ec5f-3177-bd58-6dd9ffb56dbe | -8.42587 | -48.30336 | 2025-06-25 03:45:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc787190-79f3-3841-b505-687c347b7b6a | -4.54215 | -48.01435 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4ccccdba-ebd6-3743-af7b-ace613a1c4be | -9.55015 | -40.35194 | 2025-06-25 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 5f9cc6da-0bda-391f-8d7d-75f667983d77 | -7.03058 | -44.56421 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63ca967c-9bb1-344b-a395-24b339e88c76 | -9.54712 | -40.34637 | 2025-06-25 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b9cdddc4-5157-39a8-8178-1693463d8d07 | -7.03005 | -44.56721 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80c3836b-1528-3c5e-a577-fb3c14967e8b | -5.36119 | -45.12071 | 2025-06-25 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5a5037c-23cc-3597-acfc-7e621221dca1 | -7.19144 | -43.10094 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 251fc020-1d3e-37f7-8ef7-c5009e26d33f | -7.20208 | -43.09728 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 63a9c88c-5516-3dd6-97e3-ac7e7cb1b289 | -7.0312 | -44.10287 | 2025-06-25 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcad2ae9-62dd-38ca-955e-79e24844aff3 | -4.52817 | -48.0129 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5c69d73-bdbb-3cd2-bdeb-e83a979cf5d7 | -7.19952 | -43.09601 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c98cb02b-d0a5-31ae-8045-a0b81d74539e | -4.54165 | -48.0145 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 585c32d3-5d5e-360f-9b88-0aa058c0970e | -4.54324 | -48.00805 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 09ebdccb-726a-3596-8efe-103221e1adb8 | -6.18168 | -48.06709 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 186aa066-7c29-3f47-b693-50162db57a44 | -7.19724 | -43.09645 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f54c7f92-539f-3404-9074-869822afe4c2 | -4.5358 | -48.00744 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README6.md)
