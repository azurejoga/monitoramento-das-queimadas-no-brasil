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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efb37671-ab51-37a2-af80-e4e51f919711 | -12.10779 | -45.79847 | 2026-08-08 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d44ed65c-a213-39b7-af91-dabb3a2d1d17 | -8.14246 | -55.42562 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 464ca362-fe65-31e5-90de-e48bc1e4aec6 | -7.18658 | -42.34389 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0b25cba9-a495-370a-8ab0-229d5305d2d9 | -12.35223 | -48.20844 | 2026-08-08 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f6e4883-bfaa-3e91-b24b-344268b5a501 | -10.25981 | -45.80993 | 2026-08-08 04:25:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aedd1bda-5aeb-30a2-bcf3-93a7223dbda5 | -13.37414 | -41.35087 | 2026-08-08 04:25:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a6f45cf9-2716-3f5a-b38e-44d8d861f401 | -7.18548 | -42.351 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 37dc9e89-6c51-3e2c-85d5-cc9c0d73354a | -11.26575 | -55.86237 | 2026-08-08 04:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 187076c0-ca75-3743-90a1-6d68d6250902 | -11.70684 | -50.14056 | 2026-08-08 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cb09deb-53ea-3aef-9a20-e217bc3e006f | -10.58698 | -44.79002 | 2026-08-08 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f4f52fa-36bb-3ccf-84d9-8bff103a426f | -12.54222 | -46.93653 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3de2134d-1a4e-3fe9-9cdc-32a38b217db4 | -7.16474 | -44.07161 | 2026-08-08 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdb3e16b-9ce7-38a9-bc90-092b45270643 | -6.98408 | -42.90272 | 2026-08-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c68da17-f215-363b-a4e6-8239077ceab3 | -12.52743 | -46.982 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7b32208-9b00-3d70-8fc4-56a829b5e804 | -11.31155 | -44.836 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d3aeff5-3a19-3d49-aa6a-ca60d0db1fef | -10.26941 | -45.81529 | 2026-08-08 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b4ab876-95f5-3f7c-ac43-794f0091e63b | -11.01954 | -50.53622 | 2026-08-08 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0d87c54-2ca6-38af-8be3-9f9ac996af55 | -8.15975 | -55.42035 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21e93c01-9c2b-3dd2-bd31-63e848f975fb | -11.19135 | -54.84424 | 2026-08-08 04:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ee9a1ca-5969-3565-9d4d-d8457267d17c | -12.56088 | -46.93166 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0e159f9-33ce-3c5d-b1c4-95860f57236f | -6.92806 | -41.91492 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bea1462b-c42f-3072-af7d-0211434536e8 | -6.98631 | -42.9102 | 2026-08-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| af92c7ed-8640-3099-ae6a-e05d3ff19114 | -6.97298 | -41.49076 | 2026-08-08 04:25:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e861988-b066-36bf-970d-df91bcf88725 | -7.18213 | -42.35046 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 50726f62-739b-304e-a192-2d266cacaa2f | -8.12157 | -45.89391 | 2026-08-08 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 158d6709-56c1-3393-8814-22e22ec33029 | -6.41523 | -55.78766 | 2026-08-08 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a13a58b-f060-3692-86dc-01172a904667 | -11.72909 | -50.1367 | 2026-08-08 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cc495e86-b91b-3c7b-91b3-df812e3d10f3 | -6.86203 | -46.00354 | 2026-08-08 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a19e7e08-352d-36ad-8a1f-04dc1861583f | -7.03787 | -45.5462 | 2026-08-08 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 675d6f2c-5b6a-3911-bae3-47be13a8887d | -7.18603 | -42.34745 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 67ad5e29-dc04-3447-8656-3c164db69358 | -8.54944 | -45.36667 | 2026-08-08 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca4c7728-754a-3d3b-a711-eeff795a56bf | -6.30646 | -52.81189 | 2026-08-08 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54f47a6d-18de-3501-b90f-2e2926e00c93 | -12.81998 | -41.96253 | 2026-08-08 04:25:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9354f25-c8bd-3786-a15d-eb333fd4a178 | -6.85498 | -46.00236 | 2026-08-08 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7276d59d-4e13-326a-9d09-eccc0607c796 | -12.35299 | -48.20399 | 2026-08-08 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 312462ef-09f9-3967-b9be-44fe2fa4e367 | -8.14967 | -55.42183 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2cd63c9-f546-3bf9-ad40-b82e33cd54bf | -6.91462 | -41.95715 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b42f99da-113a-38e5-b2ac-ab23220f9e2c | -12.52724 | -46.9619 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a52eaf72-6c31-3a1d-a84b-49282adcaf24 | -12.52789 | -46.95803 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cc08705-2f54-3f85-8427-82f842622579 | -11.72006 | -50.13902 | 2026-08-08 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 074392c6-1388-31bf-829e-4fd085c91629 | -7.51227 | -47.56643 | 2026-08-08 04:25:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab613f28-d0c8-31b6-be2d-d20b7dc8c1f5 | -6.42317 | -48.53887 | 2026-08-08 04:25:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3ad1c10-a23b-3772-8056-ddfd09116942 | -11.79392 | -40.92659 | 2026-08-08 04:25:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc1b8eb7-a65e-3cf6-bdff-ac77906b65fd | -13.38888 | -41.35291 | 2026-08-08 04:25:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c411c1cd-ca12-3fb4-a72b-618042b1c850 | -14.2832 | -42.2878 | 2026-08-08 04:25:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ef8bf0c6-eba9-3f76-8696-a8efe23d2242 | -12.53963 | -46.95197 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67b979a1-312b-3eb3-9f99-678932678014 | -6.97356 | -41.48702 | 2026-08-08 04:25:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4af431a7-4e49-3028-b45b-b0b326acbfc5 | -7.18098 | -42.33569 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c2b6a3ae-cddd-34a6-98eb-228eadd78a98 | -12.14099 | -48.26569 | 2026-08-08 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2ce9745-fa82-350a-ab8a-249f5ddc076e | -7.15531 | -44.06652 | 2026-08-08 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b017dc0d-92ca-397b-bd42-b3db1b0ddca4 | -11.39328 | -46.9974 | 2026-08-08 04:25:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a1b89b3-d9d0-3a12-beab-21ac735f5f2d | -11.72491 | -50.13591 | 2026-08-08 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f25eeef9-f25c-34f7-9cb0-8b0c5bf3fc4b | -7.08277 | -42.26955 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1f51467b-7f7f-34ad-be89-df42f979af2a | -8.15248 | -55.42432 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a8debf1-9fa5-3bfc-bcd9-6badf2bd2270 | -11.34153 | -45.21909 | 2026-08-08 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 795bdf09-f383-38d8-af9b-106983ad1f04 | -10.24056 | -45.79951 | 2026-08-08 04:25:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b46d2c5-969a-3162-a402-d2b17f3cfbc2 | -11.24617 | -54.01992 | 2026-08-08 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2d80563-b11e-3908-b31d-2d83955ec046 | -6.71953 | -48.11585 | 2026-08-08 04:25:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a57db4c-10ab-306b-8e77-f6fa76c72b85 | -9.38415 | -40.31848 | 2026-08-08 04:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7947f5d4-604c-3618-b94b-cf7782cbcceb | -8.16601 | -55.4216 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06b30959-8ae6-3576-a951-68f3cc448dfa | -6.91168 | -41.97183 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7c5ecd97-d0e7-3436-b3a3-432bebed9574 | -8.65851 | -45.8586 | 2026-08-08 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa463efe-0d13-3ef1-b22c-dafacf4d6ea1 | -12.34566 | -53.15812 | 2026-08-08 04:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4da1ca60-b130-3537-b818-db24e16a3923 | -10.27206 | -48.26082 | 2026-08-08 04:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 311991df-95b2-3431-a6d1-b0f2a26fcb95 | -6.91351 | -41.96435 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| eb6b409d-85f4-375c-96c6-ea5ab07ce9ae | -8.16318 | -55.41905 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d95bb151-e7bb-3055-aa29-4105f633fed1 | -8.65385 | -45.86542 | 2026-08-08 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23730812-b3c3-38bd-9043-0a7ecaf3ce29 | -6.91296 | -41.96794 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dc2cea98-19da-3de9-a8a5-611ba143e23f | -8.66907 | -45.8372 | 2026-08-08 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fcf11a8-ebdf-3f9b-bfb3-28c10980d84c | -11.68247 | -50.132 | 2026-08-08 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6d9ad65-dd09-30e0-af0f-e8b9d5edaba6 | -7.31617 | -48.09698 | 2026-08-08 04:25:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 660a8b8e-f101-3faf-a8cb-78c42039f236 | -12.54028 | -46.94809 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d005c4e9-aaec-3dc5-a787-9e80a37a5f3f | -11.31656 | -45.20398 | 2026-08-08 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b629f78-aaf0-337a-9d97-bf4bd60c044e | -8.32663 | -46.38743 | 2026-08-08 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e01302f-564b-388f-8220-fac757bc9055 | -11.30429 | -44.86013 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4907241-d9a9-35fe-8585-283366a4a298 | -8.12505 | -45.89447 | 2026-08-08 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4babf3b2-d753-3c8f-b745-ff10ec084662 | -6.60232 | -56.36429 | 2026-08-08 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc8440ba-6f4c-3435-a803-8ec0c812aa58 | -11.30818 | -44.85715 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa3e75c2-0ccc-3719-b226-b459cdabc95d | -6.99577 | -42.1022 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a362c598-6f03-3c7d-aa70-ec4af520888b | -12.54505 | -46.94093 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12d416ff-9204-3231-a1c9-62e0602c30ec | -7.08139 | -42.26969 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| be5d4a5a-6481-3693-b15c-8283b253520f | -7.0797 | -42.2585 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a62902b6-cd41-3169-992a-962f5ae210c0 | -7.51503 | -46.99863 | 2026-08-08 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c491663-ee60-312f-8e2c-4bde7f9f2d36 | -6.9111 | -41.9313 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 28cbf770-78a4-33b4-9294-c856887657c1 | -8.33306 | -46.39252 | 2026-08-08 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 426db1a6-5961-3584-b584-525b79e6aec6 | -11.30823 | -44.83545 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37aebe09-46e4-3241-abe1-57cfc6624504 | -12.33501 | -53.15908 | 2026-08-08 04:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a657d29f-8902-3bad-bc25-a25047a9c60f | -6.8585 | -46.00295 | 2026-08-08 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ec7a227-0f74-3194-8270-f2e57a7e9b54 | -8.34431 | -46.39034 | 2026-08-08 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d8c9b66-919c-3ba3-a745-e42bc9b583f8 | -7.18268 | -42.34691 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 58219fb3-1ba1-3bbf-9c9d-6433d018fc36 | -12.54441 | -46.94474 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d3f36375-3c8f-3d0c-9ca6-5c516277702f | -9.38045 | -40.31792 | 2026-08-08 04:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3abca8a2-eb75-3846-ac21-edc22911164a | -12.53506 | -46.91538 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ab4f37b-e690-3440-ad2e-57ae90932e5d | -6.98299 | -42.90968 | 2026-08-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c28b6e9e-6885-3198-a646-841c5e176bf8 | -7.16197 | -44.06758 | 2026-08-08 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfc31000-969d-3b7c-b470-0273b7e605ca | -11.24548 | -54.02344 | 2026-08-08 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8929dfe6-ed5a-3aec-9ae3-5aa6369cd4f6 | -6.60342 | -56.35858 | 2026-08-08 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4f920cc-da0e-3a16-8047-3f9cd5cc37ce | -13.39196 | -41.3312 | 2026-08-08 04:25:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dc994d29-52e2-3596-8418-1bbe1fbf4dbc | -10.24398 | -45.79993 | 2026-08-08 04:25:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deccfb39-b1f2-3088-aa29-c578c927bd01 | -11.03117 | -44.27905 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README11.md)
