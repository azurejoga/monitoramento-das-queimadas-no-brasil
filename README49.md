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
| 20a9355e-5109-37c3-af61-fca88271eb11 | -10.10678 | -44.56308 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f9e6da6-0835-38dd-a796-9a089f3397b5 | -3.51505 | -52.8453 | 2025-10-18 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7fa4234-c4e2-3c2d-b01c-b1907f66d8d5 | -7.29577 | -41.94774 | 2025-10-18 04:29:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8ac42c54-4b32-3279-9ced-74612f3669c4 | -4.25016 | -48.56914 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db334e4c-291f-3d83-91c7-569c8ee80cdd | -6.20998 | -44.67999 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6335d8e7-3eb1-39d9-acaa-b12d26f28499 | -5.57672 | -41.32059 | 2025-10-18 04:29:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dae4272e-528a-3348-91c5-4a7eda7e9604 | -6.48681 | -44.56019 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36b06e11-d086-39d4-b81d-7ad30e5493d8 | -6.30551 | -45.54294 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b05b2e5-c970-3b9f-abf4-c53482523694 | -7.67395 | -44.63439 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c274dc3b-f5da-386b-8195-cda47f4e9d4b | -5.8946 | -43.89824 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41871fbd-a824-33df-8650-adb80373ba66 | -10.29552 | -44.04183 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da86b359-3821-328d-bc27-b1809b72b563 | -7.39865 | -44.75029 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd0e25b0-bd2e-3a3f-b6cd-eca37fa6236e | -8.60368 | -40.19535 | 2025-10-18 04:29:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 91f9f209-0964-39bf-83a6-334fda8d889f | -10.24838 | -44.03469 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 04582d40-c363-3449-9474-8c169b8b3b4a | -6.86824 | -44.70836 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bd77467-bbc6-3728-9d58-37caa4ac997f | -8.35283 | -46.22313 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15c9ef34-90b9-3481-97b1-613238da1e09 | -6.31713 | -40.95133 | 2025-10-18 04:29:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e9adda6-9c4e-336b-a654-f2eb7b158949 | -6.13102 | -44.85353 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0768a5f8-1e9f-359f-9581-9388131f692a | -8.36335 | -46.19962 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4bb72e7-db7b-32ca-8141-b06114f8c0ba | -6.23209 | -44.64989 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 021564f3-60e2-3661-9ea9-b8808498f0f2 | -8.18299 | -47.04018 | 2025-10-18 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40213c31-6bb2-3ee8-ba02-f04100b54ebd | -8.82583 | -49.69419 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d63d6bbb-471e-3a0f-95ce-08a9f8e3d0ea | -9.25047 | -44.34628 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e7c95f5-a2aa-37c4-8405-e979d0ec2d29 | -7.02039 | -41.81569 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 96d7955b-7295-3654-b2e6-87e42e57b533 | -9.35235 | -46.9873 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f197beb9-2274-3318-b29b-f50edac327a5 | -7.47128 | -42.75266 | 2025-10-18 04:29:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8600d1d4-7a50-39ea-aa94-4182dd8b0ac6 | -10.43128 | -45.01793 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5db5aea-ce67-36ba-bf84-7e5216f7ba2e | -5.98866 | -44.14946 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85dd22fa-a6c6-3c14-aa62-8b23b77fadab | -10.6872 | -44.55613 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5589a36c-a34a-3f7e-8b88-87f0fa517a7c | -8.33877 | -49.96959 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39bc1dce-45e5-3c30-bca2-3b65fe312a98 | -5.76247 | -46.68707 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 786b71ad-2002-35c1-857b-2cc10a791c85 | -5.93067 | -44.95203 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a974371b-ea3b-3480-b53c-116c81ccda5f | -6.33856 | -43.93929 | 2025-10-18 04:29:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef6171b2-c000-310d-92af-bdd336fa761a | -10.49506 | -43.28428 | 2025-10-18 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9996487b-92db-34ec-8ebc-d65466fb6178 | -8.38117 | -46.23839 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd637afd-9694-3117-811e-888f1e8f988e | -7.16847 | -42.37935 | 2025-10-18 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2c74b5d3-b701-35ab-957c-52cdbceb9341 | -6.37643 | -44.7088 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74b12ba2-a602-36f6-b763-a4cb60572f3b | -7.16014 | -46.21414 | 2025-10-18 04:29:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3119e535-b0d7-38bc-8a01-b894164b7dec | -7.35039 | -46.76447 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 585d9fbd-de8a-330e-aeb9-637e48e1ded4 | -9.12925 | -46.61878 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8529b79-bbd8-3d04-b52d-7993408f9b2e | -7.66395 | -44.63739 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cda2ae92-35de-32ff-b52e-285da13e3d7e | -6.10813 | -45.84838 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3793365f-65da-3c64-b598-2a0b9149650a | -7.09411 | -44.25385 | 2025-10-18 04:29:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a61452ff-3c24-35b8-9adc-3bacc74d79fc | -10.23152 | -44.07249 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a986354-7dd2-305d-88a3-db16cafca690 | -8.10011 | -45.42797 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9eaff78-9d03-3703-9424-f5649cf296a2 | -5.8365 | -40.82187 | 2025-10-18 04:29:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6332b557-306e-3eb7-a26f-02e2d40f6393 | -5.57926 | -41.31936 | 2025-10-18 04:29:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 995ffc2d-8950-3e25-b39c-40d24819468b | -6.89223 | -45.44675 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 022381eb-cb41-37c4-ad31-60a230fc5859 | -10.64263 | -45.30811 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f57286d3-7f01-3d92-b74a-7eeac3fcef2e | -7.99845 | -45.15691 | 2025-10-18 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36d2a533-f0d4-353d-8e5e-663870e704f4 | -8.30164 | -43.39266 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c64c73f7-f9c1-3d18-aaff-de42deaa4e63 | -6.47764 | -44.57404 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db73e374-b70b-30a5-9adb-b47ae118c7d7 | -7.76952 | -42.48581 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ad355ca7-3fe7-3712-b09a-4edfcf304641 | -7.97071 | -45.15633 | 2025-10-18 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51aeccd9-97e0-3a07-b7ad-afc66ecb0b2b | -9.08519 | -48.02805 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc9fbab0-02b9-3880-bc23-6e753184804d | -7.99109 | -45.1595 | 2025-10-18 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73ad1670-1922-3173-bb2f-4494048ab7da | -5.21114 | -46.19724 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af69add2-2812-302b-a9cf-3400a0dd69fc | -6.21537 | -45.29445 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b4da139-97b5-32d1-93da-589c3eea0eb9 | -10.1679 | -46.596 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f002548f-36f1-361d-84b5-af77b145e204 | -7.06998 | -44.73463 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a44d820f-eec7-31ea-82ae-14efc470d6c7 | -6.17292 | -47.87384 | 2025-10-18 04:29:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6786a2f-7183-3ff6-9b70-f01dfdb8c748 | -10.65007 | -45.32882 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c603ad7-1ebc-3de4-a821-e007f647c44e | -10.24714 | -44.04325 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd5e6ff6-b243-3d6d-9b09-70d4fb1e431c | -6.42239 | -44.70473 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d290046-20b6-35a1-b10f-0f7484b4f433 | -5.09376 | -49.06695 | 2025-10-18 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42db7b96-6aae-3355-b096-ac71fa5011b8 | -10.12098 | -44.54069 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fce0994-17bc-363d-a09a-1e7f1e2dd0b8 | -5.33527 | -51.0001 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cacf7e9-e0c1-382c-8923-d561352478c5 | -8.27345 | -40.59794 | 2025-10-18 04:29:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce617ee9-a71a-3049-ad83-9a78d24064df | -8.46024 | -44.17034 | 2025-10-18 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07df369b-3d4a-328a-adf7-c40ce5e40f39 | -10.7899 | -44.09548 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5a0a66b-e1f5-3dcd-8259-e1f65c40d0fd | -6.96499 | -47.12189 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75961597-4899-3fca-bfec-3a660f4eb25b | -8.33586 | -49.96476 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02ec3578-ea89-35c6-a39d-675e34d6e8c9 | -10.51664 | -43.40144 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbc5b599-8519-3648-9ecd-c9bb0983dccb | -8.63326 | -54.71362 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e3a7a6f-b261-39aa-8e4c-a437c6e3ad54 | -8.24798 | -43.32915 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 79ab831d-45b8-3f09-b1fe-805bfe97a8c2 | -10.09128 | -47.63821 | 2025-10-18 04:29:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96fa4d6f-15b5-39de-9e8e-7ed7deadcc35 | -9.22564 | -48.58994 | 2025-10-18 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c82145fd-3d3d-3cce-a465-e5092cbec77e | -6.37117 | -45.7687 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30302da6-4b0b-3700-9aed-abd9a313f25a | -10.5194 | -43.88483 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bc157c5-8fd3-308e-8c2c-3e902d489298 | -10.23373 | -44.89446 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b21aa9bf-242d-3c67-9cc6-b244c32f686b | -8.16641 | -43.30548 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2673dc7d-acc5-3e68-8eea-c6eebb18aa61 | -6.59262 | -44.16159 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80bf9ce8-e348-3bc6-a7c9-1d49bb91b8a0 | -9.12909 | -45.92456 | 2025-10-18 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a3c2858-bdf2-300c-8a71-dee684073023 | -9.91206 | -47.67428 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97fce42b-962c-34a6-bbbd-53398ea8fc53 | -7.984 | -46.76164 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6e7125b-a102-3dc4-afcb-9602dd2020a1 | -6.12428 | -46.15685 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6da34a48-d48c-3e7e-8c80-5f7b14267ebc | -10.52105 | -43.39753 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f6d5b93-66e6-3263-8fcf-b2d9c13ad72a | -10.67828 | -44.56712 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff17607d-3e5d-3d31-bb58-2a83a7b90377 | -6.23265 | -44.64629 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e11f9f3-b9c1-34c8-a44c-97522acc9954 | -8.19515 | -43.3143 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 286d43f3-e6dc-3c89-9928-2c9328704a60 | -8.20681 | -46.91169 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da471682-03d6-39f0-bd27-551528ee4047 | -10.01385 | -48.07934 | 2025-10-18 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92eb78fd-1c53-3085-9520-de77368b24c4 | -9.90889 | -48.1429 | 2025-10-18 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96b745c7-584b-3e21-b07e-de207ce5ad36 | -8.95205 | -49.02192 | 2025-10-18 04:29:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7751fb62-053b-3dad-9c28-4f3b82a05168 | -8.33537 | -49.96624 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34a19d54-1d07-31d4-91a1-43bbf5b5c91b | -10.4213 | -44.91016 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0097377b-e663-3d22-9a93-988a5fd3467a | -8.53486 | -49.59924 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9a524d3-4f52-3765-aa74-fbe477aeefa2 | -6.14399 | -44.29227 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| efb4cb51-e8fa-3bcb-bf64-e185d2321f8a | -7.53859 | -43.93245 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d88e4208-9384-3198-bff0-c0cbd871e17a | -5.92873 | -45.43773 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README50.md)
