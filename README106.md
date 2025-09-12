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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34c26278-9d7e-3dfe-a275-d06540604630 | -12.83051 | -52.96772 | 2025-09-12 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 779bcd67-bd7f-3428-80d3-f232ce728d85 | -12.85906 | -52.97173 | 2025-09-12 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e6a3aac-81c5-3d99-9e13-5d940f3f3807 | -11.95541 | -51.16673 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e740e9f-9e66-3de1-83e8-0b007a91e6c3 | -10.67878 | -48.64368 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3bfe825-4659-3bc7-a747-5cc0deda8889 | -9.57718 | -57.73847 | 2025-09-12 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c1e0479-c44b-32bd-9121-20959c655423 | -10.53209 | -49.87542 | 2025-09-12 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95a15133-fc8e-348b-8bec-e8f74edec449 | -10.5366 | -51.52293 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45ce5b29-cfea-3cd2-8e8e-eadf6ee11015 | -8.8861 | -49.93452 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c53c2c2a-bc60-387a-990a-06df278fa719 | -10.38209 | -50.49918 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6b5bcdd-6bd8-3bea-9573-5eee3b3f6916 | -9.0316 | -47.09229 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 73630fcf-7556-30d4-aefb-909d86099bda | -11.17807 | -48.43063 | 2025-09-12 05:18:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3a147a7-7872-307e-b991-bc399801303e | -11.20444 | -55.07281 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ca3e2f0-08f5-301b-8e63-14d7bd8705eb | -10.67662 | -48.66148 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae8a8701-b850-3f88-ba7f-d5c6e56df9e7 | -11.52613 | -50.60852 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 379a517d-78f4-3444-95b7-f31c0dd9c3bd | -10.3575 | -57.48263 | 2025-09-12 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 13f7962f-2a63-33a3-a805-590749d7911c | -10.68311 | -48.66005 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d247bee1-6ac5-31fe-a833-ea47c5f771a0 | -11.87096 | -58.82184 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9045b13-2811-3c10-9661-311489a62bbe | -11.97201 | -51.15264 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6a6a237-868b-3fde-b224-c22e97c74603 | -8.89814 | -49.92869 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9db21b67-39b3-327f-b0d7-663cd2c242de | -11.80581 | -50.56888 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c16a334d-db81-39e3-9b66-bba85ef52346 | -8.60453 | -54.70158 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b761a7e2-ef0c-350f-a9db-88c6c408a5ab | -10.42506 | -60.47213 | 2025-09-12 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfb6399c-962c-374a-ba87-04c326653145 | -6.76466 | -56.8619 | 2025-09-12 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 012457ec-6b85-3812-bcf1-b66a01b025f8 | -10.41358 | -50.59809 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 845c6e54-9d20-3a63-920e-207cf28dc79c | -11.1994 | -55.07939 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81e533de-65b7-3f97-ad7e-8a66d4b65dfe | -11.19232 | -55.07118 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f9975c7-5234-372a-914e-fb198e83ecf8 | -9.96758 | -51.69959 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f5a6ec7-755c-3aa3-b902-32cab4a40141 | -10.13991 | -47.91182 | 2025-09-12 05:18:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| badfc677-27c0-3a10-aff8-cdcaf4292056 | -10.53621 | -51.526 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d95afca1-9624-3d4e-9ab8-e9b23ccb5114 | -9.03692 | -47.04955 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7076176d-c58e-3244-af3b-4768baf62659 | -9.42456 | -58.99214 | 2025-09-12 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4d38542-9969-30cd-b226-bb8258a6da65 | -9.07244 | -50.49766 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a60be09a-c3d6-355c-b1c1-d9afe6b6eb7d | -9.06235 | -47.04177 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 064b4a6a-8d7a-3010-9032-2ad2f5d62666 | -8.42898 | -47.25515 | 2025-09-12 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 345c194f-3287-3df0-b025-0c3b4033f89d | -9.89376 | -51.87434 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c47f1ac1-f524-3650-b2a5-da9e1c5f4f12 | -7.73984 | -47.42359 | 2025-09-12 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4f6d004-3065-3144-93f7-a4a9539a74bd | -7.22795 | -55.05473 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57664451-a678-39a6-a4c6-249abe327b04 | -9.33392 | -65.46135 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4519a408-d922-3df5-a41d-5a5e82b4ea5b | -8.48687 | -47.26906 | 2025-09-12 05:18:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e7b8c442-4035-3dd9-bbf7-5bcc695924de | -9.67731 | -47.53601 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4a782893-e082-3130-b4b2-aa92a37424f9 | -11.8732 | -58.80712 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8388529-60fe-3809-a62e-a37086a7ab1e | -10.66635 | -48.64347 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 573764df-0444-3f0a-9223-701050bee9e6 | -11.1141 | -50.71272 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e900f05-2724-3ff1-85b7-b7997dc28d36 | -9.03372 | -47.07523 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6bd19864-3636-3d16-b82e-cf20680b0393 | -9.61891 | -55.01235 | 2025-09-12 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d9e3cb1-5e1a-322e-9488-1ad26a8cddba | -7.94148 | -63.67721 | 2025-09-12 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00b962c0-2dc2-3a26-a6ac-361140a79083 | -7.40799 | -50.64632 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0f8db04-8133-3b19-a0a3-d298c68cf447 | -10.65848 | -48.65664 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94e96804-f8d2-3f04-9884-f8230c6aad13 | -10.67765 | -48.59974 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2580d5ef-85ea-311a-8a6d-3b1e7ef8ab70 | -9.34846 | -65.45192 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6e18d3f-28bc-32c1-a20f-0fa35febc57e | -11.1107 | -51.33595 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 938e14c3-6d28-3d45-88cd-b543fced9e29 | -11.22012 | -54.99051 | 2025-09-12 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eef7568d-971f-37e7-8fde-2c6c296b2863 | -8.89162 | -49.93533 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f14a5be3-f07c-3089-b294-404f660d729e | -8.49269 | -47.2753 | 2025-09-12 05:18:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5e5a3be8-e9ec-3e91-85c7-23e2a7939aad | -10.55115 | -51.53061 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8661dbab-816e-398c-9e67-421d38b9d8b1 | -11.53249 | -50.60199 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f17e79e-82bc-3431-aef4-4f8e2047287c | -10.42232 | -49.99509 | 2025-09-12 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 990dd336-4f5d-305f-90b2-c8a9c85ac83d | -9.96315 | -51.69929 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c468e6f8-38bb-3278-b64d-640306bd9a17 | -12.50698 | -47.43613 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96d198ad-501b-3d30-b174-4fec2dc261ad | -11.34188 | -61.55799 | 2025-09-12 05:18:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94afe060-9511-3adc-a736-0d3d7e0aeb68 | -11.88222 | -58.82723 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 079a30c3-8dc5-30fb-9cfd-6f6bda665009 | -7.3715 | -59.96246 | 2025-09-12 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84c7b7bf-3a97-38d9-b3af-3fcf5bba4d7a | -9.58235 | -57.75087 | 2025-09-12 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eda3572-b566-35c6-847c-38840692f073 | -9.97276 | -51.70349 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36abd0c3-478f-3c88-bbd4-ec2b637e5dfc | -10.6837 | -48.65501 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a9882a4-dd08-3079-bad2-61f70c67eaa1 | -12.86651 | -52.95121 | 2025-09-12 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b8e4c243-c6ef-3ebc-a16c-40f50f0fd6b9 | -9.1407 | -58.91512 | 2025-09-12 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b7b0293-34b0-3ca9-a61d-8a517af329de | -11.86982 | -58.8066 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31ced060-bdf4-36de-9a8f-ef10266a3e1b | -9.03231 | -47.08657 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7456d569-04c5-363d-9277-4e15c0c41d82 | -8.88106 | -49.93002 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdfe8bfc-ec2b-3d87-b3b7-ec9d70b41b27 | -9.26891 | -65.81122 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 988dba17-6eb0-3f87-bad0-5bffbd49fa28 | -9.78584 | -47.85375 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9620ce3d-17da-3e69-b94f-e1573d24c590 | -10.65304 | -48.6501 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 918d99c2-0d4a-3b94-a793-47df6f881d45 | -10.55629 | -51.49005 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a416ca2-e0d9-306b-b01d-c1ce321e9ea2 | -10.74189 | -48.9044 | 2025-09-12 05:18:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07ee44ee-81d4-3106-a8e1-c7893eebd858 | -12.85973 | -52.96645 | 2025-09-12 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ece770e6-cd38-3ff9-9ca8-b67a7e78fb5a | -11.23076 | -55.00304 | 2025-09-12 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61022c9e-66e4-3469-87db-e13ec22c0981 | -11.70477 | -48.28413 | 2025-09-12 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d6f6b549-4c29-3efa-beb1-5e62ccb222ec | -9.0491 | -47.03955 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e3257b36-f12b-3330-a440-df5b5a790dc9 | -9.74204 | -48.34504 | 2025-09-12 05:18:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bad0fe7e-61ce-3313-9cf7-0d0bf4621e77 | -10.67249 | -48.6444 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edcfd2ea-2479-359f-aff7-b2632445875c | -11.64695 | -50.58274 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b2c4ba0-668b-31e8-97c0-0bdc912db694 | -9.72218 | -64.9335 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c77aa9b-fa22-3649-9220-896363fe3775 | -9.96814 | -51.69999 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0a3a54b-3c56-38a1-9b7b-329b904685f4 | -7.94291 | -63.67488 | 2025-09-12 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b38d8efe-475d-341f-b398-b2e6eccf30d6 | -11.67348 | -58.10645 | 2025-09-12 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dfe6d6c-28ae-31f1-a2b3-44d925d46722 | -9.03907 | -65.40343 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4ee582d-0699-3749-a0e3-acddd7834b15 | -11.96917 | -51.17629 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e37bf376-85f1-3192-b3ac-30f95437e104 | -9.0243 | -64.29961 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac44ef13-4f8b-3f88-9353-3744d4d2edc6 | -8.49252 | -47.27666 | 2025-09-12 05:18:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dd683d81-0ba0-3be8-99b2-0220014be320 | -7.22842 | -55.05784 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b00b090-5c8b-3d06-839a-edff6a813c38 | -11.18368 | -48.4371 | 2025-09-12 05:18:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5ee4ac0-dbcf-3664-8f7a-2650abd8a818 | -10.08346 | -47.15816 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61f5b000-c28d-3982-a632-34a7591f49b7 | -11.95987 | -51.17418 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| e8466747-8cf7-3494-88a0-fe424ddbb32b | -9.80408 | -48.88721 | 2025-09-12 05:18:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7630735d-b10e-3177-8ef5-1112ad4b302d | -10.20119 | -51.67299 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85504c3e-698e-3563-bb40-48d5ade281d0 | -11.10323 | -51.95864 | 2025-09-12 05:18:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ecb2596-dca5-3adc-8cbe-1c5b5ff3db2c | -8.62592 | -53.12064 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 674192a6-c121-3c08-b071-d4847bfc27ce | -10.14231 | -47.90901 | 2025-09-12 05:18:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3cc2269-34ac-35fc-9f7a-c444d1128d72 | -10.85007 | -48.16718 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |


[Clique aqui para ver as próximas entradas](README107.md)
