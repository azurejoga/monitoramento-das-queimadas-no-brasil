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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea83d5b9-e024-37e5-b3d0-189b9c68ea27 | -15.02847 | -54.89571 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f5e7098-2d28-3b0b-905a-7bdfd907ef15 | -11.32715 | -47.84866 | 2025-08-23 04:53:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6b65487-b063-3819-ac37-e3bd7dbc12ed | -14.47467 | -46.0595 | 2025-08-23 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01ae3dfe-a0f4-3f4e-ae70-cdfb2a536a04 | -12.78405 | -48.71569 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16d63330-beb1-3703-b7d3-66e88cfc2609 | -12.99018 | -45.23825 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cb2e855-428d-3074-9352-975db998100f | -14.76249 | -55.98805 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbde5ea1-95c1-308c-96e2-ca7edd4082a7 | -15.71861 | -48.21524 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8353e1a0-0082-3974-9309-16094bfcaee0 | -11.20152 | -55.04057 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32585e73-68e2-3515-baab-a9e2a2a08804 | -11.62184 | -50.42946 | 2025-08-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27e048b8-5735-3f81-807f-7c06481d53d2 | -14.26526 | -58.53815 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee21e54d-10ec-3086-9afd-03b46123cc84 | -14.42574 | -53.33593 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00d397f0-bc6e-362f-91aa-bccf55be2018 | -8.89604 | -62.43385 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43a4a87d-db12-3521-a0a2-205c66f557e2 | -11.37954 | -54.3498 | 2025-08-23 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5be309f-f4a5-3c29-8024-13436ef45d63 | -13.42273 | -46.25426 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f413cf40-905a-3665-a859-5ec7ca028a89 | -14.62177 | -54.84305 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82c4d273-aa65-39ca-9321-ca7233bc8934 | -12.99212 | -45.22188 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22b055ec-47ef-3872-a839-c51fc7b54771 | -12.79649 | -48.71739 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b62079c4-2a73-3aac-bc68-faad42a852ff | -9.52968 | -60.52575 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0be6d610-5749-3149-8e57-bab82b72e5ec | -13.04368 | -46.32015 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 23db133e-a79d-305a-be9d-ebeebba67cae | -11.18756 | -55.04196 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86ece52d-1b35-32ff-991c-0909485febd4 | -11.3235 | -47.84334 | 2025-08-23 04:53:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3aa2b150-e85a-3f4f-be8f-126fcbdf6233 | -12.7768 | -48.70676 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ac440040-5f3a-3461-88d0-5d8c63f1c38c | -17.27692 | -46.77436 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 538e5ca6-5c6f-3d3a-9bba-aa89f356ff72 | -10.46269 | -59.13387 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5f36d6b-9cd3-34cc-bfd0-ba9414c2da6b | -17.2823 | -46.77176 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06c90c6f-139f-34fe-b5b7-a014def506d6 | -15.53463 | -54.76773 | 2025-08-23 04:53:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce492f84-e5b9-3e98-80cf-a3da755831c5 | -14.42239 | -53.3354 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b859eacf-313c-3629-abba-89ba1bb82b9e | -9.94854 | -60.17914 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc4bc3cc-b582-33da-ae80-020305c78288 | -13.38046 | -46.21857 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb08d71c-b480-36ff-aa8e-63a220a6dc12 | -13.33829 | -54.39573 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc7668be-5570-37c8-93e1-d45b0188bf8a | -14.81263 | -47.94659 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9a0c824c-b61b-39fb-b0d1-2424ef8540c2 | -12.98593 | -56.89714 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ad1e046-c645-3060-ab13-ca6265377246 | -16.49193 | -46.74386 | 2025-08-23 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d494cc44-a398-307e-9459-f17e36d27699 | -15.07784 | -48.50605 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7d029b71-7a02-3ce2-b065-a6b71a39f465 | -15.223 | -53.85728 | 2025-08-23 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4d5d1717-f496-34df-96b2-42e6d5d91af5 | -15.01966 | -54.88697 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e05ddd4a-6176-3b12-a7db-9e05b254ccf9 | -15.54677 | -49.90016 | 2025-08-23 04:53:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e87bdee-7373-346d-b2e2-deeba1a26c5e | -9.25824 | -59.77753 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf1309d5-98c9-38c8-beda-90c0c795ff18 | -15.20057 | -48.24491 | 2025-08-23 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e3a5629-6666-392e-a449-7e53570623b4 | -8.88611 | -62.40099 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c401240-fc96-34f8-8979-8edc26b1a003 | -14.69035 | -54.90517 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf608fc7-b5d8-337d-a3dd-850191673c0f | -9.51547 | -60.55275 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aefdae25-bd96-328c-a8ed-2f5c5060c8a0 | -14.6931 | -54.90928 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32240764-2605-3fc9-babf-f55b0c0370ad | -9.65187 | -59.64957 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0fa02061-4a6b-31ce-8ceb-5e46356e67a1 | -8.87965 | -62.43691 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2af7dce1-6e96-3a2e-9dff-52916c49e9ca | -14.61567 | -54.86027 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5022826c-ac02-3fb0-8c54-d7bfe1002682 | -8.88608 | -62.43131 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fca17bc9-e4ad-3009-baab-dbe37d70b2fc | -8.88667 | -62.42806 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b3489e3-9351-3ac0-a0fc-05a5e02fdeeb | -13.41648 | -46.26434 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc902f3f-d718-3cc3-9c82-30bf85f9a961 | -14.52411 | -57.23993 | 2025-08-23 04:53:00 | NOAA-21 | SANTO AFONSO | MATO GROSSO | Brasil | 5107263 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e0b1213-fb9f-339c-8395-2b5ffbdfc009 | -14.66659 | -54.92675 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b9481c14-9f87-3ff1-8cae-df063b20d241 | -13.33499 | -54.3952 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 313181b3-57bc-340a-840d-8996c26ef57d | -10.11051 | -57.76277 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11267c4e-ea82-34f1-98fe-604a7cd7f5ec | -14.47062 | -55.94232 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 214a1ae1-a1e8-35f4-80c5-61581c7b79d9 | -14.64981 | -54.88049 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6eddd05e-213c-39c8-86e2-7d4438c75255 | -12.94661 | -46.29675 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0420b6e0-10b4-3099-b7a0-e01a60437a0c | -14.61511 | -54.86382 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1cc4a4bb-91ca-3b9e-9298-729049400905 | -13.03269 | -56.83165 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cc8a0a0-19bb-3917-9e51-b3d6646aed4e | -11.3082 | -55.13974 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8902820-cfc6-3559-8ce9-93b5d7d48f99 | -14.90493 | -47.99403 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c198fac-e39f-3c3e-b2ed-d631ab700345 | -10.34927 | -58.60662 | 2025-08-23 04:53:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b652212-84a8-3ab2-b618-7b5dde4b3494 | -11.18929 | -55.03118 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e09b197-87db-3a42-93e5-b56190cce5e6 | -12.94426 | -46.29733 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee78ece8-c3f5-33ec-a2c9-2271f66d37f3 | -9.96032 | -60.19035 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 7578870b-2ead-3e44-8c4c-d4b6cfc4ca80 | -9.52137 | -60.5194 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9c63b40-3fb8-38a9-ae2f-be70c0347c93 | -9.51463 | -60.55748 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae7f0b9a-ebe1-33cf-819a-55bb95928eb1 | -9.52464 | -60.55433 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 050e0a60-cce0-309c-b4b9-a317d8705a2b | -13.46661 | -47.03257 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 593cdec3-a45a-3ef6-8fbd-275c7db031be | -16.51327 | -46.73445 | 2025-08-23 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9517e5b1-7e48-3d0b-a2c7-72a71a84680b | -15.07349 | -48.50555 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 90eb0aa2-28c0-3fc2-8ff7-115347c8d4f9 | -13.03334 | -56.8277 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 479d9bfb-77d8-3a78-8bdd-3a3ca59fe5ae | -15.07044 | -56.3895 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c751d880-6edc-3e02-84ef-a912eca6f8cf | -12.99251 | -45.21859 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 202753df-0942-3659-a27e-e895a10fca29 | -13.35759 | -54.40249 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05ec4d41-eb8e-3f74-b04f-6a77ad210733 | -14.8171 | -56.04607 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 235922e3-dfcd-3274-bd0d-fdb9869bed23 | -13.0305 | -56.82314 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 76829173-9e6b-3452-84c6-434d549a6ecd | -9.9626 | -60.17709 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 86f7a158-7c2f-39fc-9744-f9159b77a0b7 | -14.62017 | -54.81001 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| edf57573-be0e-3ef2-bdc8-5a2fb43a539c | -13.02506 | -56.83438 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2af42e6-5946-3d59-bb7a-5d002999933f | -8.87149 | -62.42194 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50dc9494-238f-33ba-9e35-9fc8867393b5 | -12.77629 | -48.7106 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bcb5a7f3-542a-3e4f-9aff-e35e6ff24ee4 | -14.67158 | -54.91665 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61186c23-8bdd-374f-9975-e6667f872988 | -9.82077 | -64.27231 | 2025-08-23 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47a20111-164d-314d-a19b-77e133698aed | -14.61189 | -54.81957 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7068cba7-ebc8-34e2-b534-ba1f241a9255 | -15.69963 | -48.09085 | 2025-08-23 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab4d8682-8166-3282-89ba-0f095bb190a1 | -14.66813 | -56.58793 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64f2d30b-6d55-3b9c-bc50-e97aeaf0d900 | -13.02766 | -56.81859 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d335470c-dd14-35d2-9adf-925a4dc4fd9d | -14.73857 | -56.0292 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b5cb685-76c2-36fc-8558-a23ca0c9e6e5 | -12.5098 | -53.82016 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 116def77-77f0-3b5a-b17a-3c70eaf2e3d2 | -13.4782 | -46.90424 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02d0fd34-8f55-361c-8609-d886ca3a74b4 | -15.03289 | -54.88915 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55a4395d-827a-310c-bbb0-89bfac29bcda | -13.68747 | -57.75842 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eee77e2e-18b5-3452-a44c-026e419a5af4 | -14.67736 | -56.61718 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5c63181c-2146-36f5-b1aa-d2072819529a | -12.70657 | -48.10728 | 2025-08-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0df5d7ca-ed16-3f93-b316-c27da7354a5e | -14.30619 | -58.55377 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40f519b1-7411-36b9-9d95-b1db771dcd77 | -14.33741 | -58.57372 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f204948-03f3-394b-9a73-39ac58e298fe | -11.44187 | -47.3329 | 2025-08-23 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e625282-f302-3788-a2e7-5148ea07909e | -9.52632 | -60.54479 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d0acb7d-3d9b-3fe3-98bb-cd8e8b34f7bd | -13.0279 | -56.83894 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e2bc1dd-742a-3732-969f-14dfb3351f03 | -9.94487 | -60.17393 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README53.md)
