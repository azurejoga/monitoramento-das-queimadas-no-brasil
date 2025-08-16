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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e06a8a75-f91a-3011-a8e0-f49d618114a3 | -12.77565 | -45.93817 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38ca8280-fc23-32dd-b5d0-3ab3b76d9da6 | -7.53283 | -50.52721 | 2025-08-16 04:10:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0093d32-b0d3-3b63-b744-06463c99686f | -9.81178 | -48.53936 | 2025-08-16 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ad5ad26-5720-30be-b826-c5083d268ad5 | -12.29836 | -50.01685 | 2025-08-16 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40873da9-6f73-3b8d-a7b8-25543760d8b5 | -12.56087 | -46.94735 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ac87ba50-f6e7-35d0-9b2e-1cc959467b73 | -10.53888 | -42.55043 | 2025-08-16 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ca6d165-ec50-367d-b484-3f44a2f41165 | -11.35204 | -55.4196 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8f5503f-4606-3045-8d9b-248bfe188144 | -9.36853 | -47.98334 | 2025-08-16 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6df742f5-8a4a-3cbb-aaa7-ffe939eea48c | -12.82454 | -46.00579 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0b775ac-47b8-3392-b995-7fbdcb038a65 | -11.31443 | -42.07048 | 2025-08-16 04:10:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5445bffd-3d65-30a5-9692-d46c2cb96fea | -7.97492 | -43.96367 | 2025-08-16 04:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5e4038a-7a2b-33b3-9e81-e23110ebf9ff | -12.59612 | -46.92499 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ac88246b-8b66-3e7e-ab02-f1f87edbcb8f | -13.46715 | -43.75372 | 2025-08-16 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5e34218-4869-3d4f-b29c-f41d8373e8a2 | -6.61364 | -42.75018 | 2025-08-16 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 454e86e0-b534-3413-aeab-ae7f7f57071c | -6.54648 | -43.03304 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27ec25ef-52c7-35c5-9241-573184693823 | -12.83103 | -46.03305 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e22962a2-f7e4-3825-b4a6-3d8123f16008 | -6.27518 | -44.96292 | 2025-08-16 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cffd2680-d4ac-3c77-9dfe-ceb412374db6 | -13.60755 | -46.91923 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 177c8ff3-207f-35aa-806a-5daeccd213f0 | -6.94232 | -44.56125 | 2025-08-16 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5986d337-d547-3c6c-80ff-df933f65a5e8 | -12.60616 | -46.91218 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54f57b9b-ae83-38d4-94fa-e4d72a73621a | -6.54414 | -43.04763 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ac34c4b-d6de-3acf-93d7-fae64055d622 | -8.19618 | -45.02233 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fac9c15-6e75-39c6-8bbf-b30f98e4d09d | -6.55552 | -43.04198 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a6c116d0-8c55-3940-a665-becf72d818ff | -12.59044 | -46.95789 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27e922f8-7a1c-39bd-8630-ad1e7d2ceb80 | -12.61818 | -46.9334 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 77910344-7d7b-3580-9dc0-2c31c7df2740 | -9.70671 | -46.26908 | 2025-08-16 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3205ffde-abf0-3ee2-a1fb-a4a4c20c794c | -12.61023 | -46.95697 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbec4984-1bc6-3df0-92fa-9ddd6762a023 | -12.60234 | -46.91164 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 180a0381-d22a-3f1a-946b-4b7967ee668b | -12.59584 | -46.94938 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 79223aa4-c1ae-3967-a960-959567e0f846 | -6.56666 | -43.03972 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4a8a470-39b1-3035-a2b8-37f0c6f9a448 | -5.57232 | -52.05048 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01e5d362-2a55-325a-a136-99468779ce84 | -12.61918 | -47.86985 | 2025-08-16 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51104e23-d8b4-32e7-a49d-3f82cad35cf9 | -7.14616 | -44.39164 | 2025-08-16 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bd84134-61b3-3b6e-8f98-a0fd04a15de1 | -11.36285 | -55.43472 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc15505d-839d-331f-b25b-e21509dae35e | -11.93291 | -44.12422 | 2025-08-16 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 313f2ce0-6896-3eef-a371-25f549c3b0aa | -7.40158 | -44.8808 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d441c0b7-6994-3af1-a140-aa9c1dca9c44 | -11.93351 | -44.12054 | 2025-08-16 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28f1ef68-5ca8-3e8c-8cb6-0e1a5d8b3226 | -7.26448 | -44.57798 | 2025-08-16 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87906a88-e84b-3fe6-a887-92165f1739e4 | -8.19207 | -45.02317 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baac5d57-f8b8-3070-96d6-4daf39b2194b | -12.53368 | -46.96799 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8a28180-3860-3515-a29e-acdaf6cf9695 | -12.56206 | -46.96305 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9a54aa70-9d2d-3765-8f31-856b974c00f7 | -13.62024 | -46.9132 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2281359d-614c-3cce-ba84-0946c9079485 | -13.42802 | -43.67732 | 2025-08-16 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a97d75e9-102a-3714-88c0-093c4a6f9b1d | -8.16957 | -45.0238 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2377dd46-7780-38dd-bcb1-9fc51623c43c | -11.35606 | -55.41406 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9b0784b-65fd-37ca-bc45-ec96d7f9f334 | -10.23658 | -48.30649 | 2025-08-16 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df628a83-fd50-37c6-b9e2-2a02e9f2f6a1 | -11.35983 | -55.4153 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77356cd7-39c4-3267-b3f4-cb3b276cf82a | -13.58171 | -46.97964 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10498abf-8b17-3806-bc8d-e263e3e0067d | -8.11218 | -42.35758 | 2025-08-16 04:10:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4863fc9d-71b2-3023-828f-1f95309b97ac | -12.53071 | -46.96255 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e8f0eb8-d0d0-3eff-a94d-b34613b5643f | -8.18843 | -45.02257 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec0d7b8b-1a45-3479-aec3-c8440c06d9f7 | -12.56038 | -46.97273 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78483007-a208-3884-89f7-8c51bae14650 | -8.1616 | -45.02689 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 019db2e5-475f-3468-8f4d-e831ecfeeadb | -7.24079 | -44.79182 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfbbbad6-97a7-3f6f-90c6-2ef4ce91e2e1 | -9.16574 | -45.32054 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d2950e7-416b-3d7e-890e-4d64d9982ffb | -12.55914 | -46.95729 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 5cd5799a-3f3f-32fb-a040-80ce4338c242 | -9.17232 | -45.32601 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fbbbffd-3678-3d09-90a0-31f3c6e976f8 | -12.82596 | -45.99747 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 225321cf-0e87-3404-87af-fdcbd8c4e0c8 | -11.35622 | -55.43323 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05c1a57e-bf6e-3e55-aec3-6e6d763ac57b | -8.74409 | -44.04738 | 2025-08-16 04:10:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 981e4935-6197-30a2-b63e-457abd31690b | -12.60097 | -46.96519 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e922c9c-1b2b-33f0-89cb-33bfe3a4911b | -11.34694 | -55.42455 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cafa338e-e153-31cb-bce1-2d8a27f0f8a6 | -13.56505 | -46.964 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 01bb58fd-b4e9-34d3-977c-c5c1b2ed6bed | -8.18186 | -45.01711 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef255153-78ec-3231-b24b-05c28252bfde | -12.78213 | -45.9437 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fac6668e-b279-346e-921b-de4696f4e47d | -7.5375 | -50.53137 | 2025-08-16 04:10:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07a1731a-2ebd-39b0-a9ae-525bedf6b9f8 | -6.96142 | -42.8645 | 2025-08-16 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49746e21-7f63-3993-93eb-db535bb91109 | -10.86795 | -48.48148 | 2025-08-16 04:10:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59bbfdf5-d360-3813-8b20-19bdb34d93ab | -12.05035 | -45.76403 | 2025-08-16 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7e120581-674e-33ba-a667-f4e833f96ce4 | -7.55224 | -45.41776 | 2025-08-16 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85bad1c1-4899-3dea-9f17-ff8eb6d5c506 | -6.60456 | -42.75628 | 2025-08-16 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 1ac67c8f-01db-3da3-906b-3733c3f63528 | -10.86365 | -48.48066 | 2025-08-16 04:10:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbd7d79a-ce6c-3b7d-8be8-d7fee2eb1376 | -12.82814 | -46.02816 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6f15d88-ae84-3c13-8f55-6fabef1d5049 | -8.19276 | -45.01893 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1360bc98-6fce-35a4-be28-cc8052a35e3d | -13.8708 | -45.54856 | 2025-08-16 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ae59f94-44fd-353d-9418-37cade5f54fd | -8.16593 | -45.02322 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc208a4c-7364-3f1a-934b-6a527cc2d4ab | -9.18032 | -45.323 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c3c6218-972b-39dc-922c-f6c1a4a280fb | -12.53918 | -46.95912 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 37b59d25-c21b-3067-b011-e3287326e04c | -12.83175 | -46.02883 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cd1f33f-0d03-3df9-827d-c462afcb0fb7 | -11.35359 | -55.42593 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af5bae25-1818-3732-a088-10193343063c | -7.07509 | -44.93603 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4beaeda2-e48e-3024-a566-700bd192a869 | -10.96525 | -49.57047 | 2025-08-16 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c8457631-1092-35b9-bf55-3f15b7302e3b | -11.26326 | -50.47403 | 2025-08-16 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 100ac7eb-ad56-3c91-b74e-778c1b7dd1c0 | -13.58405 | -46.96605 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6e75bc2-cfc0-3a91-ba62-e2208905bd0e | -12.43339 | -44.69697 | 2025-08-16 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8873cd15-fb2d-31bd-b08e-caaa4a50262f | -7.36057 | -43.83212 | 2025-08-16 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e2cd188-0d7a-3f6d-879e-7d86f7c275b1 | -12.82526 | -46.02329 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4371efb9-a2da-30fd-a73f-59cb68a2e41e | -8.80551 | -52.07597 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2985469-03c9-380d-8313-16c0c43b6c71 | -6.20993 | -45.92469 | 2025-08-16 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29bf3dcb-33e2-3221-8d4c-295c257aae8e | -11.25734 | -50.47859 | 2025-08-16 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dac297c9-486a-3a76-9f2a-72215bd880fa | -12.61103 | -46.95229 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1303f434-1469-3fc3-bd59-438ed9238e5f | -9.69908 | -46.26782 | 2025-08-16 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6e6a9c29-b247-3f9c-97e5-9818ce3d8e58 | -12.20824 | -47.24334 | 2025-08-16 04:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecce4517-6d89-366a-85ae-feb2d8c8a08d | -12.77924 | -45.93887 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 145018fe-52f0-372d-b15b-02e7fef37418 | -6.56631 | -43.03997 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f65adc37-33df-3bc2-b571-194915685c91 | -6.67602 | -43.76049 | 2025-08-16 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b89a0a30-c93f-3e07-9779-0a0a4d797657 | -12.79731 | -45.96369 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fbbb282-1f68-38af-ba3b-6dde36819bbf | -11.35865 | -55.42113 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec65d8b9-3deb-36d7-90ee-1b127fab4c4b | -8.74818 | -44.04408 | 2025-08-16 04:10:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c4945e5-9276-330d-9b4a-b9ec92a06059 | -6.78116 | -44.35601 | 2025-08-16 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README32.md)
