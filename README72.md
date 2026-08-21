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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac63e24a-8262-3df1-a9a3-52c6ab8ceeb5 | -12.80835 | -48.42521 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9735be32-47c3-3f71-9514-6fae968d078d | -22.62144 | -54.99886 | 2026-08-21 05:25:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5b34c5b3-2cdc-31b8-a7fc-0d9d41219dc9 | -12.80422 | -48.40968 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d449c040-1741-37d2-a3a1-b67b1310ace0 | -10.24622 | -54.37138 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbd29a02-e975-3ce8-8f89-6ae49e3a72ab | -9.41585 | -60.55122 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07c6eac0-39f9-3d94-8b92-86b6962ab0da | -11.18131 | -54.02872 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3befe94-0693-3ab2-8189-b93bf18aa450 | -11.68285 | -54.56775 | 2026-08-21 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 067028e4-1531-3189-ad94-22c222592663 | -11.21317 | -54.00254 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9b7bb0e-bba6-356e-b286-300b6dbe7828 | -10.91901 | -57.17408 | 2026-08-21 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cb79d2c-dddc-3db8-90eb-4f68516db8a2 | -9.39713 | -60.55606 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfc9a605-7e14-3541-a517-51bb82d1c6e6 | -20.25729 | -46.73829 | 2026-08-21 05:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0e84d5c-b47a-3725-85fc-ad9aa5bb85a0 | -12.12367 | -57.21324 | 2026-08-21 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be13fc71-2b43-31a0-831d-953c6b937d5a | -12.7504 | -48.46732 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e41f2b9-0e37-36fb-8f96-d197e866a72f | -9.11988 | -60.92326 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9da9dc70-f3bc-3b0a-a8f1-d20cfc4c2b8e | -12.84246 | -48.43703 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05c7864c-2b50-3bfb-99e9-c0c912e054cc | -11.21255 | -54.00411 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82429e68-f21e-343e-8cec-2bad8af6b130 | -12.84294 | -48.43298 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b7c059d-d4ba-3397-ac43-09b8576ddf87 | -9.3908 | -60.55099 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75291e07-f23d-3012-8ec3-6c82832d3317 | -11.48953 | -45.10498 | 2026-08-21 05:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efa70cee-27e6-30ac-ab03-d7b630d2c746 | -19.74507 | -57.97676 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f4e53c73-71f4-314d-99e5-475be535813e | -19.73334 | -57.95791 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 173c749b-cf37-38d4-8978-0c1fd2b40558 | -11.37321 | -46.36615 | 2026-08-21 05:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc85fdc9-0dc4-3fd9-b83f-384e4dedcb5a | -12.80322 | -48.4184 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1253720e-efa9-31b5-a454-4e961aba7914 | -12.83444 | -48.45489 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea39da4d-ea79-3ebf-9ba7-4377a06eec58 | -12.78198 | -48.39711 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba9a7fc4-279a-3b89-805c-17d6169b70cc | -9.11507 | -61.60182 | 2026-08-21 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb3216b6-cba8-3466-8157-73af522dadd3 | -11.21648 | -54.00472 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12c72a3f-eeb4-388e-8d2c-c9eba9f064b7 | -19.72862 | -57.96564 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| a4806df3-5ff1-3321-8bf4-cceb4473cb7d | -11.20188 | -55.05104 | 2026-08-21 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f80c4e35-163d-3fd2-9b7c-6bf9fd1d7ec9 | -12.86088 | -48.43144 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 572361f7-d6d6-355f-80fd-50747be6dc48 | -17.96345 | -49.37599 | 2026-08-21 05:25:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 718758c2-2195-3a15-a4e0-86523735de78 | -11.18276 | -54.01875 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f390086f-87c4-3783-b033-b98252385121 | -10.24177 | -54.37533 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff3aa103-85a8-36b4-94f9-b80a3d48a509 | -9.23669 | -60.3879 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a02366d0-36ce-3729-92ce-aae89fa12c6b | -9.40708 | -60.43055 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ca52ba4a-661c-3d55-abfc-5d97ccf113f2 | -9.413 | -60.54675 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f72cea18-5b6f-3595-bac2-4171ce159d14 | -20.29075 | -46.74124 | 2026-08-21 05:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c9bbeb5-00a2-35a4-8c86-8b3104476d39 | -9.41782 | -60.40861 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41b4a285-efff-3084-838f-ad27f3f11a1b | -10.38674 | -61.21201 | 2026-08-21 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccb34ee3-07dd-3d51-803e-f100bf9cffea | -11.68218 | -54.57246 | 2026-08-21 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75309796-a6df-3803-83a2-2559b9a1797d | -11.67837 | -54.57186 | 2026-08-21 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b919ebf-e944-3113-b25f-d219bc4bcf2d | -9.41088 | -60.40745 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 966dd3e1-ed51-3ea8-bba8-5add8060e432 | -11.21104 | -55.06589 | 2026-08-21 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b94a2b28-890e-3fa9-b160-3faa2c8bc4b9 | -9.4014 | -60.42169 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a4417b20-7245-346a-aee0-281485b2ef00 | -12.73132 | -48.47891 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 901e381f-e8ed-3f2b-95ff-944d4fe60ae7 | -9.40297 | -60.43382 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 543104d0-a7b1-357d-b3a0-ec9cc4319afa | -10.38741 | -61.20796 | 2026-08-21 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e70f9cd9-8639-314a-8f82-d4d03d4aff36 | -9.40539 | -60.54948 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e90c43f-21c6-36bf-8296-94b0eaeadf19 | -17.95669 | -49.37584 | 2026-08-21 05:25:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 221d245b-4a2a-3aae-8b73-16168ce33101 | -9.54333 | -63.56715 | 2026-08-21 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713013e0-5b13-3b02-84e6-016293e11124 | -22.62197 | -54.99446 | 2026-08-21 05:25:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 09f45418-8a48-327f-b8eb-5496fd226ae7 | -12.49621 | -54.75206 | 2026-08-21 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f61d4ed8-6a2e-3540-ab44-208cb339e65b | -12.80906 | -48.42226 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32a55e09-e130-3594-8879-d6ee08ed12f4 | -11.20531 | -54.00142 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d28616f2-d9f5-38bb-b5f2-381a9eb4a864 | -9.41372 | -60.41188 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 8e56c824-c6d2-30ab-8697-b9bdacda290f | -9.40992 | -60.43496 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5ad35570-8bf4-3908-8991-5863c33993a0 | -9.41529 | -60.42398 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 928db8c2-43c3-3c37-b8ba-178b9f095aa6 | -11.16172 | -54.02588 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3c3c9936-e16c-3b88-b70a-ed29691d1355 | -10.77745 | -50.30257 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fe428be-2ded-3ed9-b90f-5b9f7eb26a59 | -9.42066 | -60.41303 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fc3622e-d27a-3f30-ad8b-047d14eeb18a | -19.73274 | -57.96206 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ed4b1ea4-305e-3b68-8264-57c5a46f24a0 | -9.12389 | -61.5943 | 2026-08-21 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63cb1aa9-a33e-36b2-bc87-4e2cbc8ae4d8 | -19.74273 | -57.9679 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7a436c4e-d2f4-3a19-a4f5-0b62f0d74d4c | -9.39172 | -60.56716 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87a9ff58-a380-3e78-8edb-dcb200d444a9 | -19.73156 | -57.97036 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ff53a87c-41c4-3f3a-a733-d0cbca9423bc | -9.38951 | -60.55877 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc6b5f68-711e-3010-8cd1-bd00370a9ae1 | -18.03401 | -46.46408 | 2026-08-21 05:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6c7e4a9-dbb8-3918-9661-bd8db0b9c60f | -12.73752 | -48.47633 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2d77a9b-45ae-38d1-8745-26ed60240358 | -9.39015 | -60.55487 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 091db58d-022a-38ba-9459-b634ae718b03 | -12.8544 | -48.4361 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb3a6850-182a-3939-b876-a29b9c2e65fd | -9.4235 | -60.41744 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e01b5443-cff4-337c-a4d8-3300273554bd | -19.73449 | -57.97506 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 58d96452-7117-34c4-bf3f-6e8918daf996 | -11.20799 | -55.06096 | 2026-08-21 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6830cb4f-7788-348f-a6fd-d497809ca420 | -11.18741 | -54.01428 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e81e4bd-dc86-3551-9199-347cb805263b | -9.41402 | -60.43169 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a015643-3d9b-3936-97ea-0e337229acc1 | -23.53509 | -47.32068 | 2026-08-21 05:25:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8fb2d49d-7f92-3e8c-8d33-454813d4eff3 | -11.17099 | -54.01705 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b1667bb1-be7f-35a8-b187-03721bd0f1f5 | -9.11948 | -61.59805 | 2026-08-21 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e00f550e-0ae1-37ec-bf0f-a32469a9bf11 | -9.38887 | -60.56266 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f116cb12-12b1-3794-8f9a-0690766ef46c | -9.393 | -60.55937 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f3a954f-56af-30c7-8c72-9382b273a14c | -9.41719 | -60.41245 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43a2c818-aa42-35e6-aa67-a894250ec525 | -12.00724 | -53.43163 | 2026-08-21 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a7f9f8ab-79b8-3070-97c0-55e4eb757992 | -11.20863 | -54.00354 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c438daaa-a3d9-3d7c-b4cb-974352b1fc15 | -20.03759 | -57.18951 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edf253c8-647d-3c97-ac52-d5753f0ef51f | -9.4194 | -60.42071 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc7d3f27-7a4f-385e-9c76-5b25c151caec | -22.18532 | -48.7441 | 2026-08-21 05:25:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a74f0b60-60cf-354e-a0d2-193ac995ce44 | -11.17244 | -54.00697 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22cb275c-de15-3914-90ff-e2da588a505d | -10.63336 | -51.60365 | 2026-08-21 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80d32c75-dcac-3f61-9711-88021d5e2707 | -9.41713 | -60.54346 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23a2d79-94b2-3a7e-bd39-206886fef71e | -12.79838 | -48.4128 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a484f85c-b0f0-3c2d-ba1d-be0dcea86863 | -11.16707 | -54.01647 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 47de1a86-8454-3079-be9a-0dedfae207bd | -9.40928 | -60.43881 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4786bda4-2565-34ff-9954-f7c9cc7a1ba5 | -12.75596 | -48.4701 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a85a5cb5-c7bc-3326-bf51-20c981270600 | -19.73805 | -57.95016 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b67707cb-5a77-3566-a101-09d6cadfebc0 | -19.74154 | -57.97619 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 823834dd-0187-3cb7-9a65-1441937fd534 | -20.67372 | -57.19997 | 2026-08-21 05:25:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5049731b-d71d-3e45-b1e0-ef6037b17057 | -9.24214 | -60.79394 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7faff6e3-4b51-32f0-bc02-08985bcc43d9 | -12.73173 | -48.47549 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48d8ab78-d128-3b7e-852b-653015692d59 | -9.4175 | -60.43227 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84e2e092-4504-36e4-bdc7-60c9c516b792 | -12.86141 | -48.42698 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README73.md)
