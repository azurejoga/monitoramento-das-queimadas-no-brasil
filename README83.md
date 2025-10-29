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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f61a7a1-fd46-3b9a-8c83-dc9d9f93acae | -10.87257 | -46.02936 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 446d0fa7-fd89-3af6-9e06-a15d67941b74 | -13.41705 | -42.34362 | 2025-10-29 12:19:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 48.9 |
| f843d3ec-a43e-3d8f-aa4a-5947ba5199af | -14.2658 | -48.09966 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1622e417-092c-3910-b33a-ae0c78b080c1 | -8.2482 | -46.90161 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 78615ecb-a89a-3b50-aca9-1fa8a2ade88f | -15.31377 | -48.04452 | 2025-10-29 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6efcb305-9878-3ae0-91db-9b333bbd72d8 | -9.90684 | -44.91454 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2bc6f120-c730-311c-a260-91bc88693802 | -10.77348 | -47.8891 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 5be55f1f-0f83-3713-b196-1dd1d3fc3a54 | -14.48035 | -45.60435 | 2025-10-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 62902acb-2bb8-3891-898d-5c0dab6b7289 | -8.88771 | -47.52963 | 2025-10-29 12:19:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d2c1b39c-7934-3b10-ae79-0a3718250201 | -10.36689 | -47.56908 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1b83d8e7-0a63-3b7a-99d2-faf01b890d30 | -10.92619 | -47.66338 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a1176e7b-a8fe-30e9-aba8-f6453bd6affb | -11.30865 | -47.56413 | 2025-10-29 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ed95ea35-126c-309b-b3b4-9cd3fafafcec | -12.7036 | -46.31213 | 2025-10-29 12:19:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fc172286-525d-3eb8-9eac-086a34642f96 | -10.11198 | -46.55972 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b1315531-5680-3c0b-be2e-ef21150f509b | -10.56573 | -49.84054 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6e255f9b-858d-3bfb-b2fc-e714e93867ac | -12.51397 | -47.10685 | 2025-10-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ee6df2b7-0e16-30d5-b41c-a8f5c3789879 | -13.95669 | -43.19276 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 6ad89d37-8804-3123-ad0c-850563358abf | -10.6648 | -48.00514 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f0180344-eeae-3758-932c-b89089f74589 | -12.52438 | -49.57861 | 2025-10-29 12:19:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c40fb78d-0eff-3610-a0f5-25ba9c1a3572 | -13.27545 | -47.73169 | 2025-10-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ac75cdfe-2a4d-31b7-a35e-8ffb868975e8 | -12.14536 | -45.20214 | 2025-10-29 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0c51db9a-2200-3c57-8c2f-41527248c44d | -12.76816 | -46.6613 | 2025-10-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 24be685d-27dc-3313-aa89-6e83970a5d98 | -12.38175 | -46.58332 | 2025-10-29 12:19:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0a44828d-31c5-3e97-8887-482cdfa3cc56 | -8.18672 | -46.94895 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 89c93a36-8af8-3961-ab73-fa9236073e09 | -12.0065 | -46.77744 | 2025-10-29 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| b71699c0-7a4a-3227-95d2-52c4846d46cb | -8.03209 | -47.39059 | 2025-10-29 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8971e697-7076-3601-8672-75ea70348613 | -7.3709 | -47.6253 | 2025-10-29 12:19:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 1911e943-3f7d-3008-9c83-5dc0d0be1c33 | -8.40178 | -46.92595 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 283a7d7c-02a8-3a74-9abd-0af22cc5e71c | -13.69023 | -47.18848 | 2025-10-29 12:19:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fd41177b-2e4d-3704-ace6-2fdf2c4a5947 | -11.90425 | -50.0289 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d6771108-88cb-374a-a441-dc291ac30368 | -15.35959 | -47.91257 | 2025-10-29 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5fdf0401-704a-30b2-a35e-ca506e68ce86 | -9.23747 | -46.35809 | 2025-10-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 8c208e8b-8ddf-36bc-bd27-38e085d2b8ed | -8.18856 | -44.47185 | 2025-10-29 12:19:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 143fe831-7786-3833-8605-1c37669e376d | -8.45551 | -45.88202 | 2025-10-29 12:19:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 5add5184-1058-3742-8acb-e95388d969f6 | -15.10783 | -47.93758 | 2025-10-29 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b4d19c17-dd0c-36c0-add1-cd32e98a27df | -13.64647 | -47.04184 | 2025-10-29 12:19:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3d9a651f-f18d-3c95-a57f-498a80b49697 | -7.97067 | -46.71324 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3a3bc997-e3ad-3f9c-9c40-8d7050d2704c | -8.25575 | -46.91839 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 5177f28e-4f22-33b9-94c3-190fe2c79014 | -10.87118 | -46.03986 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 30794787-827f-3a7e-bade-35ca33541b70 | -8.05703 | -45.14519 | 2025-10-29 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 408af59e-c40d-3122-a1ec-c55ab989fed5 | -13.66372 | -47.17464 | 2025-10-29 12:19:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2d4dc6ad-b8f4-3d07-9b93-00aa5ac2c28d | -10.11986 | -46.57069 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c552d802-c353-3d3c-806f-2a45435b5965 | -9.272 | -47.03329 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0f52caad-8324-3854-83c9-3e66298bc4b2 | -8.73182 | -45.21177 | 2025-10-29 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fce27c9c-eea7-396d-988c-92f0d1a0a504 | -13.22007 | -47.05167 | 2025-10-29 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0a122304-8309-3153-9683-500fe408aba8 | -11.24527 | -52.84403 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 06276bef-59ac-3156-bdb4-3adcb07c41d5 | -8.44611 | -45.88089 | 2025-10-29 12:19:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f2048713-6bee-36df-9ad2-eba1969fa39c | -12.32782 | -48.0474 | 2025-10-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a416bd7c-a6b1-33f9-a204-70e9e53920c0 | -7.92642 | -45.50136 | 2025-10-29 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 17af51bf-235b-3883-b9b8-f408f483ba09 | -13.41364 | -42.72143 | 2025-10-29 12:19:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 7981c066-2ada-37c5-aff2-59b3857221d2 | -7.71061 | -46.99098 | 2025-10-29 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e1a371b5-90c8-357e-931c-a632deda55d5 | -14.47164 | -45.59032 | 2025-10-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0ad82eca-9e47-38d1-a536-f1ebeffe46f8 | -15.16894 | -47.20973 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 73232357-889d-36dc-af8a-d78d4d6a58fa | -7.78535 | -46.45684 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 3c88b65e-ce53-33d2-88ba-ae5545c732b6 | -12.01581 | -46.77871 | 2025-10-29 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b163f99f-b3ff-37ca-bd17-1a1fc76dc50e | -9.08664 | -47.8223 | 2025-10-29 12:19:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 145351a7-3e51-3be7-883f-8867124214ca | -10.59966 | -49.60968 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 7fe9ce07-0cf2-3833-bf98-2527f572ad64 | -9.90341 | -44.93228 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 70c4042e-0927-3be1-b59d-815df5a534f4 | -14.26451 | -48.10907 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3343371f-9281-3bff-ae6d-ea06500ce1e5 | -8.05075 | -45.04337 | 2025-10-29 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 460f02ee-87d0-3f37-b0e5-b817ab715be9 | -12.76963 | -46.65046 | 2025-10-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f80a8986-2c5d-378e-a77c-5fc05f293903 | -10.47191 | -47.47832 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| bf29b3e8-57dc-315c-a188-afa2e76ddfdd | -13.61699 | -48.38998 | 2025-10-29 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9e7f88e8-a496-34d8-9e87-7e8016c4bffc | -12.37428 | -50.15887 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 910c482d-38cf-3aa7-9965-255423191245 | -13.42482 | -48.57377 | 2025-10-29 12:19:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 538f552b-cc5a-350f-9ef6-d81e412bb299 | -7.79703 | -46.4394 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e291adef-e95b-3d2b-980a-53167ff68e23 | -9.92338 | -47.1199 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0b7b8e66-0fae-3ada-8bf8-85bb1ff21b14 | -11.56191 | -47.92646 | 2025-10-29 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3d0d3144-0e65-3f87-a906-ee73e9344a70 | -11.02517 | -49.85459 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e706ecaa-8e17-36cc-b2df-ba546fea4346 | -16.17427 | -43.41596 | 2025-10-29 12:19:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 6e157346-53ed-388c-92bd-5344df948b44 | -9.03018 | -47.50707 | 2025-10-29 12:19:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7b83994d-1da3-32ee-8f95-16f257916524 | -13.09189 | -53.46333 | 2025-10-29 12:19:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5cf050ad-1f6b-3b44-a703-8c5b8b6af26d | -8.21253 | -47.29128 | 2025-10-29 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 997d8566-39c6-3a4b-a4c5-01d19fe2e452 | -7.79573 | -46.44876 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| dd273090-b428-30c6-9b72-af446e962d24 | -7.8048 | -46.45008 | 2025-10-29 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 20a14d5a-2ea4-339c-9f78-0421cb1abf05 | -9.28998 | -47.03574 | 2025-10-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| f48ea5ad-8288-3041-a0c5-2d2ba02418a1 | -13.57416 | -47.15597 | 2025-10-29 12:19:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9e3d9dbd-a22d-3705-9cd7-85f75586b36f | -8.0041 | -46.20824 | 2025-10-29 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1f9312fe-bde8-326f-9244-ca5da8c868bd | -12.71463 | -46.30289 | 2025-10-29 12:19:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| d5e747ce-1e78-3f5f-bf93-05801babb023 | -10.51766 | -47.80629 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 75511535-4234-3005-8467-6be13bc70dfe | -13.94576 | -48.48074 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 11809d30-6880-355c-be6b-ddcea657fe7c | -13.06116 | -43.04259 | 2025-10-29 12:19:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 450956ef-6cc3-3966-bcff-e31ac5f9277f | -17.13388 | -45.38028 | 2025-10-29 12:19:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 16aa7871-98db-37b6-9d11-1d588501e253 | -14.27956 | -47.3147 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| b347848a-342a-3609-8792-4a6dd65be595 | -15.32049 | -47.85751 | 2025-10-29 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8e43582e-2c7d-3348-a820-c9f00d2fb241 | -10.86098 | -50.09132 | 2025-10-29 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 5a3d22e3-8e7f-3f1e-8eb7-c3042510aed6 | -11.67459 | -47.25042 | 2025-10-29 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 060678d6-e89b-3bc7-b9d4-1d4b6593c56d | -13.94198 | -48.44279 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 41bdc822-f4f8-33a0-9d04-00a8636b6809 | -12.09913 | -47.1739 | 2025-10-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| ddf8c66f-5030-374a-846d-3da335ea5db6 | -12.06607 | -46.62055 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f9fce715-cf6a-310f-b705-e56d0ae905ae | -12.85461 | -48.62957 | 2025-10-29 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0d76f751-295b-34b2-8a5f-cb5f18f65748 | -13.32586 | -47.4346 | 2025-10-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5677beaa-bb80-3e88-b5a1-1c606bccbbdd | -12.16561 | -46.56662 | 2025-10-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 36f2869b-1a72-3af2-9cad-1fe704804380 | -14.14889 | -45.32743 | 2025-10-29 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0e58249e-3969-3e22-9445-e0e2aebdd5d8 | -11.40205 | -47.75179 | 2025-10-29 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6742ff8d-7353-3c30-95a4-26ff4f95e85a | -10.10388 | -46.61824 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f6f8906d-8653-3663-9d75-967c6ce3c4d2 | -13.23188 | -48.57029 | 2025-10-29 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| acf58b43-8d3c-3311-b680-034012e6c0c0 | -16.35203 | -43.10349 | 2025-10-29 12:19:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 29.6 |
| d064eeda-37c8-3ccd-a60f-ce8f2f532eed | -8.03082 | -47.39952 | 2025-10-29 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 194c42ba-b865-366f-b8b6-a50894edab0a | -9.92965 | -47.66782 | 2025-10-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |


[Clique aqui para ver as próximas entradas](README84.md)
