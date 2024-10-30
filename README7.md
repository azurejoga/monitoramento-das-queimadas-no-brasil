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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae878411-9056-3c1d-8db7-0460f459774d | -12.18561 | -40.86124 | 2024-10-30 00:30:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 680d4ad0-949f-3e6c-b5d6-9018d0f0a519 | -12.1253 | -39.40598 | 2024-10-30 00:30:00 | TERRA_M-M | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7f33983e-2adb-39e0-80ba-9d5b7bf6220f | -11.99498 | -44.43179 | 2024-10-30 00:30:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 73c946a5-85b7-3418-a632-21969bfc12a1 | -11.88659 | -43.82346 | 2024-10-30 00:30:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3e50d56b-e729-3b46-8ec3-3a60b625a480 | -11.87699 | -43.8248 | 2024-10-30 00:30:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 04cc20e3-58ed-3f1f-b0e1-77743e85d921 | -11.66479 | -44.96423 | 2024-10-30 00:30:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 637ceec4-cdb4-3d6e-b7c1-b1488bf577d7 | -11.61269 | -43.91182 | 2024-10-30 00:30:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fb095fa1-215a-3d0a-9fa9-c8498674d91a | -11.27401 | -45.08426 | 2024-10-30 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 11a9b5cd-05ef-3213-8b40-2ef7d886557b | -11.06335 | -45.37077 | 2024-10-30 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2c107629-74a3-31db-9d31-d050a6fe0dcb | -11.05643 | -45.36484 | 2024-10-30 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ab891b50-0826-36c9-88f2-263400f10ee9 | -10.89022 | -44.41023 | 2024-10-30 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 91eaf6bd-6d16-3190-9dd0-909ca304a92a | -10.8767 | -44.53833 | 2024-10-30 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 953abfd1-9693-3273-a057-bf96ebaf489d | -10.87058 | -44.41298 | 2024-10-30 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f392e593-6741-334e-b41d-44e3b38821cc | -10.84076 | -44.2593 | 2024-10-30 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71eeaeb0-f0ce-36de-b0fa-020d86cfa53f | -10.71401 | -44.93465 | 2024-10-30 00:30:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 38.9 |
| e94b2a1f-9d6e-363c-bca4-05c23c0c98e8 | -10.71243 | -44.92264 | 2024-10-30 00:30:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| c55c7686-21d9-395f-bb43-798915600e7f | -10.63541 | -44.88462 | 2024-10-30 00:30:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 423783b8-46fe-3749-896b-63ca77904e3f | -10.61293 | -44.94277 | 2024-10-30 00:30:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 4edb7e48-2809-3d20-a3d9-92d9331550ae | -10.50601 | -36.77814 | 2024-10-30 00:30:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 5dd85413-c122-3940-80d1-73e1972181ff | -10.50145 | -45.11083 | 2024-10-30 00:30:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 401afbe3-1170-3f2e-988b-2bf1876057bc | -10.14812 | -44.02689 | 2024-10-30 00:30:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 75423bd2-0ff6-3e28-86ca-0bc3094f4d1e | -10.14283 | -44.02327 | 2024-10-30 00:30:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 211e6cf1-efc9-3093-91a2-0dc1812f752e | -9.58378 | -46.64347 | 2024-10-30 00:30:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 96db26cc-3fe6-3e20-b2a0-9348403b217a | -8.15219 | -47.1706 | 2024-10-30 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7831fa8a-1b26-32ed-b874-8638c946b63d | -8.05949 | -47.08691 | 2024-10-30 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a7eff990-5714-3fd2-b102-dee1345e58d6 | -7.88806 | -46.90464 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f9f26f89-6f2e-34b6-bed5-a7786b08a01b | -7.87867 | -46.92107 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| de311fe9-f87a-3699-b1de-940c6ff4d8d1 | -7.87679 | -46.90623 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d0d59e16-b3f1-3a1e-b6ce-211c5a344b17 | -7.8749 | -46.89137 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e254e867-e04e-3fe6-a821-d449bdd1bdc9 | -7.86626 | -46.91352 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 463d6c2b-a91b-3cad-b546-59b62dc290c1 | -7.86552 | -46.90779 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| d7dbeba2-c605-3cc2-bd91-49af7c056f7c | -7.86428 | -46.8987 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 23489a53-6e98-3061-adc2-ea02651375a2 | -7.86364 | -46.89294 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 9a92e0ca-1522-3e9a-a506-d99298f4a7bf | -5.94113 | -40.89276 | 2024-10-30 00:33:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 38458424-d2da-3191-91e5-4f784e2f4f54 | -7.66741 | -47.32945 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d02178a1-6040-399f-8ae4-ae3792a038a5 | -7.58434 | -47.12369 | 2024-10-30 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 586c2fc7-5e8d-3c9a-8d8c-a65ebc33d8a8 | -7.57534 | -46.4413 | 2024-10-30 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 908c1089-88e7-3347-b852-4d6e5e102f4a | -7.48548 | -47.15777 | 2024-10-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f0bedb0b-e4ff-3ce8-b61b-a9666e277396 | -7.42738 | -46.62766 | 2024-10-30 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 67042573-ed20-344f-953d-f9d6844e635d | -7.34416 | -48.49182 | 2024-10-30 00:33:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8446ad87-fff8-352d-a7e2-a5f1ce825e67 | -7.24835 | -46.57742 | 2024-10-30 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 547e61eb-1121-3d08-97e0-3b4f26edae4e | -7.18446 | -45.49236 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8b003abb-856c-35d9-a30b-a02843cb313d | -7.1829 | -45.48077 | 2024-10-30 00:33:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8a890390-d04a-3869-a755-34ec516c5eff | -7.06508 | -44.8239 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ead15e33-8949-399a-97fc-73f14eef017e | -7.06467 | -45.66913 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e0f0214b-d5a2-3bac-abd4-b273d6c792d7 | -6.8822 | -46.83714 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9d334fdc-d965-32bd-b690-4f3c077b894e | -6.67104 | -44.70058 | 2024-10-30 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 83ff4742-2259-3fdb-abfa-487df7502d4b | -6.66318 | -47.09168 | 2024-10-30 00:33:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2e5ba5a9-dfbc-3524-8620-d8b414390316 | -6.66156 | -44.70184 | 2024-10-30 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7782ad86-74d4-3199-8f49-84a5e18c8a5d | -6.04662 | -46.59864 | 2024-10-30 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9090f2b1-bcb4-3b66-b27c-e6c689d6a1b7 | -6.03899 | -44.78843 | 2024-10-30 00:33:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e5fdc9c1-be73-3d89-94e1-71e92323e0c1 | -5.34083 | -43.10923 | 2024-10-30 00:33:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f89f420f-e662-3974-8593-76bc72fda52d | -5.97691 | -46.60071 | 2024-10-30 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 23cf2186-ed6d-34d9-a32f-67bf84bd5486 | -5.97403 | -45.37994 | 2024-10-30 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| bf6f477d-1f7d-38f1-ab07-7db2b4829981 | -5.97255 | -45.36901 | 2024-10-30 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 01151bd5-a26f-3856-82b7-a8c9bf3a3e91 | -5.92094 | -44.52462 | 2024-10-30 00:33:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fad6fc7f-5680-379f-82b7-b52d508a72a4 | -5.81287 | -44.13164 | 2024-10-30 00:33:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd90d548-262d-3c40-ab09-4b3add41ac37 | -5.80494 | -44.27832 | 2024-10-30 00:33:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9292139d-3d36-3d50-aef6-f7c8a007be93 | -5.75541 | -45.56929 | 2024-10-30 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2685434b-e46d-3ef0-836e-217a5fda24f7 | -5.75329 | -45.56448 | 2024-10-30 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8f9df7eb-0d53-3e7a-adc7-b09162cc6f22 | -5.73865 | -47.04014 | 2024-10-30 00:33:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 11485521-1985-3a43-8d10-98223eead306 | -5.72762 | -47.04147 | 2024-10-30 00:33:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8d34a783-eaa2-36aa-b855-290e210d327e | -5.60119 | -46.25464 | 2024-10-30 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2ee46a66-3c9d-367e-8253-a733747bdae5 | -5.55476 | -44.33197 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0e741518-01ea-388c-9c45-9bd1d77d6630 | -5.55345 | -44.32238 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 35b16996-fef3-3760-bb99-ce5070b63bdf | -5.45977 | -45.50967 | 2024-10-30 00:33:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 74c70cc2-7bb2-3650-9def-3dc2a24be263 | -5.45826 | -45.49872 | 2024-10-30 00:33:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| dd66ac54-671c-3879-8df6-1f76e9faef58 | -5.44683 | -44.42157 | 2024-10-30 00:33:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dc1e9672-ca21-39c5-8a87-fd263726b5e9 | -5.3417 | -44.18939 | 2024-10-30 00:33:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f46e2f5c-6792-3fcd-a3ff-91bb8ae92e21 | -5.29958 | -44.94571 | 2024-10-30 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 71c30209-138a-392b-9bd9-969b31b77b96 | -5.29816 | -44.93544 | 2024-10-30 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ce5d1dfa-db76-3fc8-a728-e5db68f8a0aa | -5.22985 | -46.07051 | 2024-10-30 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3cb9d408-c5b2-3418-bc67-3bcc4b0afff1 | -5.22653 | -44.90404 | 2024-10-30 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4b3e9e3f-a69a-308f-9c14-3192715369dd | -5.21708 | -44.90522 | 2024-10-30 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b7050b0f-3e08-322c-adf9-39c078231f6a | -5.21309 | -44.94722 | 2024-10-30 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ef5ee0fc-b13b-3a1a-beda-5ce39eb0b4fe | -5.20727 | -44.94356 | 2024-10-30 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b4046f7f-9c4e-3df6-a071-399803d893ca | -5.11472 | -45.15085 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e15c1180-ec94-36dd-ac97-a9315e03c86b | -5.10869 | -45.70619 | 2024-10-30 00:33:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ed2adb95-b659-37d4-8968-9246dcf042eb | -5.09679 | -44.8111 | 2024-10-30 00:33:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e10f0b03-a73f-33be-aa59-9e9da768500d | -5.06142 | -44.22742 | 2024-10-30 00:33:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cf03a6a9-372c-307e-8368-73086a37d908 | -5.06013 | -44.21799 | 2024-10-30 00:33:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 94b43de9-59f5-3acc-9273-2fe231930b98 | -5.05384 | -45.16509 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 23749f59-c2f4-38cc-834e-f387bc2fa4a4 | -5.03821 | -46.93792 | 2024-10-30 00:33:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c980c715-90be-3332-b1c2-74ff1c6b6168 | -5.00707 | -44.36675 | 2024-10-30 00:33:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| b8c526a7-f169-3b33-8d9a-6ec6b6f3a022 | -5.00576 | -44.35723 | 2024-10-30 00:33:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e56db842-0336-3b41-a2fb-1a9b4c509445 | -4.99921 | -44.37754 | 2024-10-30 00:33:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ee0a5969-7b30-3b6a-9e1c-889a856d418b | -4.9979 | -44.36804 | 2024-10-30 00:33:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| cb5f4b83-ba0c-346b-8303-0613c76ab7cf | -4.87042 | -44.382 | 2024-10-30 00:33:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 40777394-8972-3153-81f1-9d3a6eb90292 | -4.85868 | -45.44105 | 2024-10-30 00:33:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4d04a98f-5718-37d4-8fa5-ec26cb5ebd79 | -4.8487 | -46.89334 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a18c3039-6ec3-38e2-8f38-3afdf6e4012f | -4.8341 | -45.71683 | 2024-10-30 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9352345f-ce0f-3c8c-95bc-f3c16e0442ba | -4.82424 | -45.71812 | 2024-10-30 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eae57d35-9298-34ce-8284-cf2964f955c4 | -4.76569 | -44.15347 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6c6dd9d6-785c-39dd-9b5c-355ef3f93527 | -4.76303 | -48.06109 | 2024-10-30 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 569a6d76-2664-345c-8e60-bd8ef766c3dd | -4.76082 | -48.0446 | 2024-10-30 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 2cd49945-c365-3a33-9aa6-b51457b23159 | -4.74771 | -44.0896 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d90ebf0b-81fa-3d34-9e21-d3f8127aad79 | -4.74629 | -45.89476 | 2024-10-30 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0c8c2437-188a-36eb-b5af-ff7f89fda0a8 | -4.73688 | -46.66171 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24fad842-aba2-3236-b698-e90ab4c04cce | -4.70522 | -45.74042 | 2024-10-30 00:33:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 7e8f042f-7986-32d5-a714-0bff75effbd5 | -4.70368 | -45.72902 | 2024-10-30 00:33:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |


[Clique aqui para ver as próximas entradas](README8.md)
